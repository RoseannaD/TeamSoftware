import yfinance as yf
import matplotlib.pyplot as plt
import time

class DataSet:
    stock_name = None
    start_date = None
    end_date = None
    stock_code = None
       
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

# Calculate moving average
mavg = stock_1['Adj Close'].rolling(window=100).mean()

plt.plot(DataSet_Obj.stock_data["Open"]) # Plot Open
plt.plot(DataSet_Obj.stock_data["High"]) # Plot High
plt.plot(DataSet_Obj.stock_data["Low"]) # Plot Low
plt.plot(DataSet_Obj.stock_data["Close"]) # Plot Close
plt.plot(mavg) # Plot Moving Average
plt.title('{} stock price'.format(DataSet_Obj.stock_data.upper())) # Graph title
plt.ylabel('Price')  # Y-axis label
plt.legend(['Open','High','Low','Close','Moving Avg'], loc='upper left') #Legend
plt.show() #Display graph
