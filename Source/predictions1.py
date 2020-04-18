import yfinance as yf
import pandas as pd
import numpy as np

class parameters:

    time_steps = 15 #how many days of historical data to look back at to predict the next day's price
    future_days = 30 #how many days to predict ahead of the last date from the training dataset

class dataset:
    stock_code = "RYCEY"
    start_date = "2005-01-01"
    end_date = "2020-04-09" 
    df = yf.download(stock_code, start_date, end_date)


    def load_model(self):
        #load model
        model = load_model('/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/new_5.65/outputs/lstm_best_7-3-19_12AM/'
                           'dropout_layers_0.4_0.4/best_model.h5')
        return model
        
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
            self.model = load_model('/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/new_5.65/outputs/lstm_best_7-3-19_12AM/'
                           'dropout_layers_0.4_0.4/best_model.h5')

        if selected_stock_var == "PFE":
            self.model = load_model('/Users/riteshsookun/OneDrive/Uni/Coding Projects/LSTM/new_5.65/outputs/lstm_best_7-3-19_12AM/'
                           'dropout_layers_0.4_0.4/best_model.h5')

        if selected_stock_var == "RYCEY":
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

    forecast = None
    forecast_dates = None


