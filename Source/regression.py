import pandas as pd
import yfinance as yf
import dateutil.relativedelta
from datetime import *
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import socket

#global var to store stock code user wants to analyse using regression
stock_name = "MSFT"

#global var to store dataset
lr_df = "a"
svm_df = "a"
#global var to store confidence level
confidence = 0
lr_confidence = 0
svm_confidence = 0


class parameters:
    #how many days to predict ahead of the last date from the training dataset
    future_days = 30

class DataSet:

    def get_data(self):
        global stock_name

        end_date = date.today()

        #minus 6 months from current date and convert to correct format
        start_date = end_date - dateutil.relativedelta.relativedelta(years=5)
        start_date = start_date.strftime("%Y-%m-%d")

        #convert current date to correct format
        end_date = (end_date.strftime("%Y-%m-%d"))

        #raise exception if no stock code is entered
        if len(stock_name) == 0:
            raise ValueError("Enter a stock code")

        # Retrieve stock data
        stock_data = yf.download(stock_name, start_date, end_date)

        return stock_data

class prepare_data():
    dataSet_obj = DataSet()
    parameters_obj = parameters()

    x_train = None
    x_test = None
    y_train = None
    y_test = None
    x = None
    y = None
    svr_rbf = None
    lr = LinearRegression()
    future_dates = None
    lr_confidence = None
    svm_confidence = None
    lr_prediction = None
    svm_prediction = None

    df = None


    def retrive_dataset(self):
        self.df = self.dataSet_obj.get_data()

        #raise exception if no data exists
        if len(self.df) == 0:
            raise ValueError("No data found, please try another stock")

    def manipulate_data(self):
        # Get the Adjusted Close Price
        self.df = self.df[['Adj Close']]

        #create prediction column from 'adj close' but shifted 'future_days' value
        self.df['Prediction'] = self.df[['Adj Close']].shift(-self.parameters_obj.future_days)

    def convert_data(self):
        #create x dataset
        self.x = np.array(self.df.drop(['Prediction'],1))

        #Remove the 'future_days' rows from the end
        self.x = self.x[:-self.parameters_obj.future_days]

        #create y dataset
        self.y = np.array(self.df['Prediction'])

        self.y = self.y[:-self.parameters_obj.future_days]

    def split_data(self):
        # Split the data into 80% training and 20% testing
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, train_size=0.8, test_size=0.2)

    def build_model(self):
        #build and train SVM model
        self.svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
        self.svr_rbf.fit(self.x_train, self.y_train)

        #train LR model
        self.lr.fit(self.x_train, self.y_train)

    def determine_confidence(self):
        global confidence
        global lr_confidence
        global svm_confidence

        #SVM confidence
        svm_confidence = self.svr_rbf.score(self.x_test, self.y_test)
        print("svm confidence: ", self.svm_confidence)

        #LR confidence
        lr_confidence = self.lr.score(self.x_test, self.y_test)
        print("lr confidence: ", self.lr_confidence)


    def generate_predictions(self):

        # x_prediction to be the last 'future_days' rows of the adj close column
        x_prediction = np.array(self.df.drop(['Prediction'],1))[-self.parameters_obj.future_days:]

        self.lr_prediction = self.lr.predict(x_prediction)

        self.svm_prediction = self.svr_rbf.predict(x_prediction)

        parameters_obj = parameters()
        #create future dates and add to dataframe
        self.future_dates = pd.bdate_range(pd.datetime.today(), periods=parameters_obj.future_days, weekmask=None)

        global lr_df
        global svm_df

        lr_df = pd.DataFrame(data=self.lr_prediction, index=[self.future_dates],
                                  columns=["LR Prediction"]).rename_axis("Date")
        svm_df = pd.DataFrame(data=self.svm_prediction, index=[self.future_dates],
                                   columns=["SVM Prediction"]).rename_axis("Date")


    def graphing(self):
        global lr_df
        global svm_df
        global lr_confidence
        global svm_confidence

        if lr_confidence > svm_confidence:
            global confidence
            confidence = round(lr_confidence * 100, 2)
            print("Linear Regression model has a ", (lr_confidence - svm_confidence) * 100, "% higher confidence")
            print(self.lr_prediction)
            plt.plot(self.df['Adj Close'], color='black')
            plt.plot(self.future_dates, lr_df, color='orange')
            plt.ylabel("Price")
            plt.xlabel("Date")
            plt.legend(['Historical Data', 'LR Forecast'], loc='upper left')  # Legend
            plt.show()
        else:
            confidence = round(svm_confidence * 100, 2)
            print("Support Vector Machine has a ", (svm_confidence - lr_confidence) * 100, "% higher confidence")
            print(self.svm_prediction)
            plt.plot(self.df['Adj Close'], color='black')
            plt.plot(self.future_dates, svm_df, color='orange')
            plt.ylabel("Price")
            plt.xlabel("Date")
            plt.legend(['Historical Data', 'SVM forecast'], loc='upper left')  # Legend
            plt.show()

    def convert_df_export(self):
       #SVM dataset
        global svm_df
        svm_df['Date'] = svm_df.index

        #swap coloumn positions
        columns_titles = ["Date", "SVM Prediction"]
        svm_df = svm_df.reindex(columns=columns_titles)

        #LR dataset
        global lr_df
        lr_df['Date'] = lr_df.index

        # swap coloumn positions
        columns_titles = ["Date", "LR Prediction"]
        lr_df = lr_df.reindex(columns=columns_titles)

class Compile():

    #dataset_obj = DataSet()

    #function to check internet conectivity by pinging Google's DNS server
    def internet_check(self, host="8.8.8.8", port=53, timeout=3):

        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            return False

    def compile_predictions_regression(self, stock_code):
        prepare_data_obj = prepare_data()

        global stock_name

        if self.internet_check() == 0:
            raise Exception("No internet connectivity")
        else:
            stock_name = stock_code

            prepare_data_obj.retrive_dataset()
            prepare_data_obj.manipulate_data()
            prepare_data_obj.convert_data()
            prepare_data_obj.split_data()
            prepare_data_obj.build_model()
            prepare_data_obj.determine_confidence()
            prepare_data_obj.generate_predictions()
            prepare_data_obj.graphing()

    def compile_predictions_regression_export(self, stock_code):
        prepare_data_obj = prepare_data()

        global stock_name

        if self.internet_check() == 0:
            raise Exception("No internet connectivity")
        else:
            stock_name = stock_code

            prepare_data_obj.retrive_dataset()
            prepare_data_obj.manipulate_data()
            prepare_data_obj.convert_data()
            prepare_data_obj.split_data()
            prepare_data_obj.build_model()
            prepare_data_obj.determine_confidence()
            prepare_data_obj.generate_predictions()
            prepare_data_obj.convert_df_export()



