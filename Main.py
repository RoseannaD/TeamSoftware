import yfinance as yf
import matplotlib.pyplot as plt
import time


class RawData:
    def __init__(self, stock, start, end):
        # Retrieve stock data
        self.stock_data = yf.download(stock, start, end)


#store required inputs
stock_code = input ("Enter stock code: ")
start_date = input ("Enter start date: ")
end_date = input ("Enter end date: ")

stock_1 = RawData(stock_code, start_date, end_date)

# Calculate moving average
mavg = stock_1['Adj Close'].rolling(window=100).mean()

plt.plot(stock_1["Open"]) # Plot Open
plt.plot(stock_1["High"]) # Plot High
plt.plot(stock_1["Low"]) # Plot Low
plt.plot(stock_1["Close"]) # Plot Close
plt.plot(mavg) # Plot Moving Average
plt.title('{} stock price'.format(stock_1.upper())) # Graph title
plt.ylabel('Price')  # Y-axis label
plt.legend(['Open','High','Low','Close','Moving Avg'], loc='upper left') #Legend
plt.show() #Display graph
