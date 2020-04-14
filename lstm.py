# need to use Python 3.7.5 due to tensorflow. 

import yfinance as yf
import numpy as np
import time
import pickle
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras.layers import LSTM, Dense
from keras import optimizers

       
class Lstm_Parameters:
    # parameters for LSTM
    p_epochs = None
    p_time_steps = None
    p_batch_size = None
    p_lr = None

    def epochs(self):
        return self.p_epochs

    def time_steps(self):
        return self.p_time_steps

    def batch_size(self):
        return self.p_batch_size

    def lr(self):
        return self.p_lr
    
class DataSet:
    stock_name = None
    start_date = None
    end_date = None
    stock_data = None
    
class GenerateModel:
    
    Lstm_Parameters_Obj = Lstm_Parameters()
    x_train_1 = None

    def create_model(self):
        # it is possible more layers (and different parameters) need to be added here. 
        # need to complete rest of the code so a train vs test graph can be displayed before tweaking
        model = Sequential()

        model.add(LSTM(100, batch_input_shape=(self.Lstm_Parameters_Obj.batch_size(),
                                               self.Lstm_Parameters_Obj.time_steps(), self.x_train_1.shape[2]),
                       dropout=0.0, recurrent_dropout=0.0, stateful=True, return_sequences=True,
                       kernel_initializer='random_uniform'))
        model.add(Dense(1, activation='sigmoid'))
        optimizer = optimizers.RMSprop(lr=Lstm_Parameters_Obj.lr())

        model.compile(loss='mean_squared_error', optimizer=optimizer)
        return model

DataSet_Obj = DataSet()
Lstm_Parameters_Obj = Lstm_Parameters()

DataSet_Obj.stock_code = input("Enter stock code: ")

safe = 1

DataSet_Obj.start_date = input("Enter start date: ")

# Basic date check doesn't account for leap years
while safe > 0:
    safe = 0
    # check start date
    if DataSet_Obj.start_date[4] != "-":
        print("Invalid Format YYYY-MM-DD")
        correct = correct + 1
    if DataSet_Obj.start_date[4] == "-":
        data = DataSet_Obj.start_date.split("-")
        num0 = int(data[0])
        num2 = int(data[1])
        num1 = int(data[2])
        if (num1 < 1 or num1 > 12):
            safe = safe + 1

        if (num1 == 1 or num1 == 3 or num1 == 5 or num1 == 7 or num1 == 8 or num1 == 10 or num1 == 12):
            if (num2 < 1 or num2 > 31):
                safe = safe + 1

        if (num1 == 4 or num1 == 6 or num1 == 9 or num1 == 11):
            if (num2 < 1 or num2 > 30):
                safe = safe + 1
        if (num1 == 2):
            if (num2 < 1 or num2 > 28):
                safe = safe + 1

        if (num0 > 2020 or num0 < 1990):
            safe = safe + 1

DataSet_Obj.end_date = input("Enter end date: ")

# Basic date check doesn't account for leap years
safe = 1
while safe > 0:
    DataSet_Obj.end_date = input("Enter end date: ")
    safe = 0
    # check end date
    if DataSet_Obj.end_date[4] != "-":
        print("Invalid Format YYYY-MM-DD")
        correct = correct + 1
    if DataSet_Obj.end_date[4] == "-":
        data = DataSet_Obj.end_date.split("-")
        num0 = int(data[0])
        num2 = int(data[1])
        num1 = int(data[2])
        if (num1 < 1 or num1 > 12):
            safe = safe + 1

        if (num1 == 1 or num1 == 3 or num1 == 5 or num1 == 7 or num1 == 8 or num1 == 10 or num1 == 12):
            if (num2 < 1 or num2 > 31):
                safe = safe + 1

        if (num1 == 4 or num1 == 6 or num1 == 9 or num1 == 11):
            if (num2 < 1 or num2 > 30):
                safe = safe + 1
        if (num1 == 2):
            if (num2 < 1 or num2 > 28):
                safe = safe + 1

        if (num0 > 2020 or num0 < 1990):
            safe = safe + 1

# Retrieve stock data
DataSet_Obj.stock_data = yf.download(DataSet_Obj.stock_code, DataSet_Obj.start_date, DataSet_Obj.end_date)

# Check if stock data was successfully imported
if len(DataSet_Obj.stock_data) == 0:
    raise Exception("No data found, please try another stock")

# Calculate moving average
mavg = DataSet_Obj.stock_data['Adj Close'].rolling(window=100).mean()

# display graph of historical data
plt.plot(DataSet_Obj.stock_data["Open"]) # Plot Open
plt.plot(DataSet_Obj.stock_data["High"]) # Plot High
plt.plot(DataSet_Obj.stock_data["Low"]) # Plot Low
plt.plot(DataSet_Obj.stock_data["Close"]) # Plot Close
plt.plot(mavg) # Plot Moving Average
plt.title('{} stock price'.format(DataSet_Obj.stock_data.upper())) # Graph title
plt.ylabel('Price')  # Y-axis label
plt.legend(['Open','High','Low','Close','Moving Avg'], loc='upper left') #Legend
plt.show() #Display graph

# split stock_data into two datasets (training and test) with a 80/20 split
x_train_split, x_test_split = train_test_split(DataSet_Obj.stock_data, train_size=0.8, test_size=0.2, shuffle=False)

# check if the training dataset is big enough that is needed to create a model. If not, exit the application
if len(x_train_split) > 2500:
    print("Sufficient data available for training")
else:
    sys.exit("Not enough data available for training \n Please try choosing a longer date duration. \n If this is not"
             " possible due to the stock being a relatively new, please choose another stock")

# scale dataset betwen 0 and 1 
scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train_split)
x_test = scaler.transform(x_test_split)

# check for any values in train dataset that are not a number (NaN)
if np.isnan(x_train).any() == False:
    print("No NaNs are found in train and test datasets")
else:
    raise Exception("Dataset contains NaNs values which may affect the LSTM model.")
