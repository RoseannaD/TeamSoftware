# need to use Python 3.7.5 due to tensorflow. 
import yfinance as yf
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential, load_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import socket
from dateutil import parser

#global variable to store user's stock they want to analyse using LSTM
selected_stock_var = 0

#global variable to store predictions
forecast = "a"

#model date
model_date_g = "a"

class parameters:

    time_steps = 15 #how many days of historical data to look back at to predict the next day's price
    future_days = 30 #how many days to predict ahead of the last date from the training dataset

class dataset:

    def get_data(self, end_date):
        global selected_stock_var
        global model_date_g

        model_date_g = end_date


        end_date = parser.parse(end_date, dayfirst=True).strftime("%Y-%m-%d")
        print(end_date)

        #get historical data for selected stock
        #INTC stock
        if selected_stock_var == "INTC":
            stock_code = "INTC"
            start_date = "1981-01-01"
            #end_date = "2020-04-16"  # 2020-04-09

            df = yf.download(stock_code, start_date, end_date)
            return df

        #PFE stock
        if selected_stock_var == "PFE":
            stock_code = "PFE"
            start_date = "1973-01-01"
            #end_date = "2020-04-10"  # 2020-04-09

            df = yf.download(stock_code, start_date, end_date)
            return df

        #RYCEY stock
        if selected_stock_var == "RYCEY":
            stock_code = "RYCEY"
            start_date = "2005-01-01"
            #end_date = "2020-04-13"  # 2020-04-09

            df = yf.download(stock_code, start_date, end_date)
            return df


class prepare_data:

    #create class objects
    parameters_obj = parameters()
    dataset_obj = dataset()

    scaler = None
    close_df = None
    close_test = None
    date_test = None
    close_train = None
    close_train_val = None
    date_train = None
    date_val = None
    x_close_train = None
    x_close_test = None
    df = None

    selected_stock = None

    model_date = None

    import os
    dirname = os.path.dirname(__file__)
    #filename = os.path.join(dirname, 'assets/models')

    import sys, os
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(application_path, 'assets/models')

    intc = "/intc_16-04-20.h5"
    pfe = "/pfe_16-04-20.h5"
    rycey = "/rycey_08-04-20.h5"

    def extract_model_date(self):
        #extract date from filename
        if selected_stock_var == "INTC":
            self.model_date = self.intc[(self.intc.find('_') + 1): (self.intc.find('_') + 9)]

        if selected_stock_var == "PFE":
            self.model_date = self.pfe[(self.pfe.find('_') + 1): (self.pfe.find('_') + 9)]

        if selected_stock_var == "RYCEY":
            self.model_date = self.rycey[(self.rycey.find('_') + 1): (self.rycey.find('_') + 9)]

    def load_correct_model(self):

        global selected_stock_var

        #load the correct model based on the selected stock
        if selected_stock_var == "INTC":
            self.model = load_model(self.filename + self.intc)

        if selected_stock_var == "PFE":
            self.model = load_model(self.filename + self.pfe)

        if selected_stock_var == "RYCEY":
            self.model = load_model(self.filename + self.rycey)

    def retrieve_dataset(self):
        self.df = self.dataset_obj.get_data(self.model_date)


    def manipulate_raw_data(self):
        #convert raw dataset's index to a column
        #self.df = self.dataset_obj.get_data()
        self.df['Date'] = self.df.index

        #drop data that is not needed from dataset
        self.df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)

        #store close prices from dataset to close_data variable
        self.close_df = self.df['Close'].values
        self.close_df = self.close_df.reshape((-1,1))

    def split_data(self):
        # split stock_data into two datasets (training, val and test) with a 80/20(training/test) split on raw data, then
        #training is split again to create val
        close_train_old, self.close_test = train_test_split(self.close_df, train_size=0.8, test_size=0.2, shuffle=False)
        date_train_old, self.date_test = train_test_split(self.df['Date'], train_size=0.8, test_size=0.2, shuffle=False)

        self.close_train, self.close_train_val = train_test_split(close_train_old, train_size=0.8, test_size=0.2, shuffle=False)
        self.date_train, self.date_val = train_test_split(date_train_old, train_size=0.8, test_size=0.2, shuffle=False)

    def normalise_data(self):
        #scale the feature MinMax, build array
        x = self.close_train
        self.scaler = MinMaxScaler()
        self.x_close_train = self.scaler.fit_transform(x)
        self.x_close_test = self.scaler.transform(self.close_test)

    #forecast = None
    forecast_dates = None


    def predict(self, future_days, model):
        close_data_1 = self.scaler.transform(self.close_df.reshape(-1, 1))

        prediction_list = close_data_1[-self.parameters_obj.time_steps:]

        for _ in range(future_days):
            x = prediction_list[-self.parameters_obj.time_steps:]
            x = x.reshape((1, self.parameters_obj.time_steps, 1))
            out = model.predict(x)[0][0]
            prediction_list = np.append(prediction_list, out)
        prediction_list = prediction_list[self.parameters_obj.time_steps - 1:]

        return prediction_list

    def predict_dates(self, future_days):
        last_date = self.df['Date'].values[-1]
        prediction_dates = pd.date_range(last_date, periods=future_days + 1).tolist()
        return prediction_dates

    def generate_predictions(self):
        global forecast
        #generate predictions using saved model
        forecast = np.array(self.predict(self.parameters_obj.future_days, self.model)).reshape(-1, 1)
        self.forecast_dates = self.predict_dates(self.parameters_obj.future_days)

    def inverse_transform(self):
        global forecast
        #undo scaling from -1 to 1 into readable values
        self.close_test = self.scaler.inverse_transform(self.x_close_test.reshape(-1, 1))
        forecast = self.scaler.inverse_transform(forecast)

    def graphing(self):
        global forecast
        # build and display graph
        plt.figure()
        plt.plot(self.df['Date'], self.close_df, color='black')
        plt.plot(self.forecast_dates, forecast, color='blue')
        plt.legend(['Historical Data', 'Forecast'], loc='upper left')  # Legend
        plt.show()

    def convert_df_export(self):
        global forecast

        forecast = pd.DataFrame(data=forecast, index=[self.forecast_dates],
                             columns=["LSTM Predictions"]).rename_axis("Date")

        forecast['Date'] = forecast.index

        # swap coloumn positions
        columns_titles = ["Date", "LSTM Predictions"]
        forecast = forecast.reindex(columns=columns_titles)

class Compile:
    #create class objects
    parameters_obj = parameters()
    dataset_obj = dataset()
    prepare_data_obj = prepare_data()

    #function to check internet conectivity by pinging Google's DNS server
    def internet_check(self, host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            return False

    def compile_predictions_lstm(self):
        if self.internet_check() == 0:
            raise Exception("No internet connectivity")
        else:
            self.prepare_data_obj.extract_model_date()
            self.prepare_data_obj.load_correct_model()
            self.prepare_data_obj.retrieve_dataset()
            self.prepare_data_obj.manipulate_raw_data()
            self.prepare_data_obj.split_data()
            self.prepare_data_obj.normalise_data()
            self.prepare_data_obj.generate_predictions()
            self.prepare_data_obj.inverse_transform()
            self.prepare_data_obj.graphing()


    def compile_predictions_lstm_export(self):
        if self.internet_check() == 0:
            raise Exception("No internet connectivity")
        else:
            self.prepare_data_obj.extract_model_date()
            self.prepare_data_obj.load_correct_model()
            self.prepare_data_obj.retrieve_dataset()
            self.prepare_data_obj.manipulate_raw_data()
            self.prepare_data_obj.split_data()
            self.prepare_data_obj.normalise_data()
            self.prepare_data_obj.generate_predictions()
            self.prepare_data_obj.inverse_transform()
            self.prepare_data_obj.convert_df_export()
