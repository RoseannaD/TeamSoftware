# need to use Python 3.7.5 due to tensorflow. 

import yfinance as yf
import pandas as pd
import numpy as np
from keras.models import Sequential, load_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

#global variable to store user's stock they want to analyse using LSTM
selected_stock_var = 0

#global variable to store predictions
forecast = "a"

class parameters:

    time_steps = 15 #how many days of historical data to look back at to predict the next day's price
    future_days = 30 #how many days to predict ahead of the last date from the training dataset

class dataset:

    def get_data(self):
        global selected_stock_var

        #get historical data for selected stock
        #AMD stock
        if selected_stock_var == "AMD":
            stock_code = "AMD"
            start_date = "2005-01-01"
            end_date = "2020-04-10"  # 2020-04-09

            df = yf.download(stock_code, start_date, end_date)
            return df

        #PFE stock
        if selected_stock_var == "PFE":
            stock_code = "PFE"
            start_date = "2005-01-01"
            end_date = "2020-04-10"  # 2020-04-09

            df = yf.download(stock_code, start_date, end_date)
            return df

        #RYCEY stock
        if selected_stock_var == "RYCEY":
            stock_code = "RYCEY"
            start_date = "2005-01-01"
            end_date = "2020-04-13"  # 2020-04-09

            df = yf.download(stock_code, start_date, end_date)
            return df


class prepare_data:

    #create class objects
    parameters_obj = parameters()
    dataset_obj = dataset()

    df = dataset_obj.get_data()

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

    selected_stock = None

    def load_correct_model(self):

        global selected_stock_var

        #load the correct model based on the selected stock
        if selected_stock_var == "AMD":
            #need to change to relative path and load correct model
            self.model = load_model('/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/new_5.65/outputs/lstm_best_7-3-19_12AM/'
                           'dropout_layers_0.4_0.4/best_model.h5')

        if selected_stock_var == "PFE":
            #need to change to relative path and load correct model
            self.model = load_model('/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/new_5.65/outputs/lstm_best_7-3-19_12AM/'
                           'dropout_layers_0.4_0.4/best_model.h5')

        if selected_stock_var == "RYCEY":
            #need to change to relative path
            self.model = load_model('/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/new_5.65/outputs/lstm_best_7-3-19_12AM/'
                           'dropout_layers_0.4_0.4/best_model.h5')


    def manipulate_raw_data(self):
        #convert raw dataset's index to a column
        self.df = self.dataset_obj.get_data()
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
        columns_titles = ["Date", "LSTM Prediction"]
        forecast = forecast.reindex(columns=columns_titles)

class Compile:
    #create class objects
    parameters_obj = parameters()
    dataset_obj = dataset()
    prepare_data_obj = prepare_data()

    def compile_predictions_lstm(self):

        self.dataset_obj.get_data()
        self.prepare_data_obj.load_correct_model()
        self.prepare_data_obj.manipulate_raw_data()
        self.prepare_data_obj.split_data()
        self.prepare_data_obj.normalise_data()
        self.prepare_data_obj.generate_predictions()
        self.prepare_data_obj.inverse_transform()
        self.prepare_data_obj.graphing()
        self.prepare_data_obj.convert_df_export()
