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
        
#create class objects
parameters_obj = parameters()
dataset_obj = dataset()

#store model into variable
model = dataset_obj.load_model()

#summarize model
print(model.summary())

#convert raw dataset's index to a column
dataset_obj.df['Date'] = dataset_obj.df.index

#drop data that is not needed from dataset
dataset_obj.df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)

#store close prices from dataset to close_data variable
close_df = dataset_obj.df['Close'].values
close_df = close_df.reshape((-1,1))
