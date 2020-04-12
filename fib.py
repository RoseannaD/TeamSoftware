import yfinance as yf
from dateutil import parser
import dateutil.relativedelta

class DataSet:
    stock_name = None
    start_date = None
    end_date = None
    stock_data = None


DataSet_Obj = DataSet()

DataSet_Obj.stock_code = input("Enter stock code: ")

#parse current date in the right format
DataSet_Obj.end_date = input("Enter current date: ")
DataSet_Obj.end_date = parser.parse(DataSet_Obj.end_date)

#minus 6 months from current date and convert to correct format
DataSet_Obj.start_date = DataSet_Obj.end_date
DataSet_Obj.start_date = DataSet_Obj.end_date - dateutil.relativedelta.relativedelta(months=6)
DataSet_Obj.start_date = (DataSet_Obj.start_date.strftime("%Y-%m-%d"))

#convert current date to correct format
DataSet_Obj.end_date = (DataSet_Obj.end_date.strftime("%Y-%m-%d"))
print (DataSet_Obj.end_date)
print (DataSet_Obj.start_date)

# Retrieve stock data
DataSet_Obj.stock_data = yf.download(DataSet_Obj.stock_code, DataSet_Obj.start_date, DataSet_Obj.end_date)

plt.plot(DataSet_Obj.stock_data["Close"], color='black')

minimum_price = DataSet_Obj.stock_data.Close.min()
maximum_price = DataSet_Obj.stock_data.Close.max()

#calculate Fibonacci levels (using golden ratios)
diff = maximum_price - minimum_price
level1 = maximum_price - 0.236 * diff
level2 = maximum_price - 0.382 * diff
level3 = maximum_price - 0.618 * diff
