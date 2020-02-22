import yfinance as yf
import matplotlib.pyplot as plt

#store required inputs
stock_code = input ("Enter stock code: ")
start_date = input ("Enter start date: ")
end_date = input ("Enter end date: ")

# Retrive stock data
stock_data = yf.download(stock_code , start_date, end_date)

# Calculate moving average
mavg = stock_data['Adj Close'].rolling(window=100).mean()

plt.plot(stock_data["Open"]) # Plot Open
plt.plot(stock_data["High"]) # Plot High
plt.plot(stock_data["Low"]) # Plot Low
plt.plot(stock_data["Close"]) # Plot Close
plt.plot(mavg) # Plot Moving Average
plt.title('{} stock price'.format(stock_code.upper())) # Graph title
plt.ylabel('Price')  # Y-axis label
plt.legend(['Open','High','Low','Close','Moving Avg'], loc='upper left') #Legend
plt.show() #Display graph
