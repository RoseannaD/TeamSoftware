import yfinance as yf
from dateutil import parser
import dateutil.relativedelta
from matplotlib import pyplot as plt
import ta

start_date = "01-01-2019"
end_date = "31-12-2019"
stock_code = "AMD"
period = 5
lookback = 5

bb = "a"
roi = "a"
atr = "a"
will_r = "a"

class Dataset:

    def get_data(self):
        global stock_code
        global end_date
        global start_date

        # parse current date in the right format
        # end_date = date.today()
        end_date = parser.parse(end_date)

        # minus 6 months from current date and convert to correct format
        start_date = end_date
        start_date = end_date - dateutil.relativedelta.relativedelta(months=6)
        start_date = (start_date.strftime("%Y-%m-%d"))

        # convert current date to correct format
        end_date = (end_date.strftime("%Y-%m-%d"))
        # print (end_date)
        # print (self.DataSet_Obj.start_date)

        # Retrieve stock data
        stock_data = yf.download(stock_code, start_date, end_date)

        # Clean NaN values
        #stock_data = ta.utils.dropna(stock_data)

        return stock_data

class Prepare_data:

    df = None
    DataSet_Obj = Dataset()

    def retrive_dataset(self):
        self.df = self.DataSet_Obj.get_data()

    def add_timestamp_df(self):
        self.df['Timestamp'] = self.df.index

    def bollinger_bands(self):
        # Initialize Bollinger Bands Indicator
        bb = ta.volatility.BollingerBands(close=self.df["Close"], n=20, ndev=2)

        # Add Bollinger Bands features
        self.df['bb_mavg'] = bb.bollinger_mavg()
        self.df['bb_hband'] = bb.bollinger_hband()
        self.df['bb_lband'] = bb.bollinger_lband()

    def rate_of_change(self):
        global period
        self.df['roi'] = ta.momentum.roc(close=self.df['Close'], n=period)

    def average_true_range(self):
        global period
        atr = ta.volatility.AverageTrueRange(high=self.df['High'], low=self.df['Low'], close=self.df['Close'], n=period)
        self.df['atr'] = atr.average_true_range()

    def williams_r(self):
        global lookback
        self.df['williams r'] = ta.momentum.wr(high=self.df['High'], low=self.df['Low'], close=self.df['Close'], lbp=period)


    def graphing_all_bb(self):
        #bollinger bands
        plt.plot(self.df['Close'], color='green')
        plt.plot(self.df['bb_mavg'], color='red')
        plt.plot(self.df['bb_hband'], color='red')
        plt.plot(self.df['bb_lband'], color='red')
        plt.show()

    def graphing_roi(self):
        #rate of change
        fig, axs = plt.subplots(2)
        axs[0].plot(self.df['Close'], color='green')
        axs[1].plot(self.df['roi'], color='red')
        plt.show()

    def graphing_average_true_range(self):
        #rate of change
        fig, axs = plt.subplots(2)
        axs[0].plot(self.df['Close'], color='green')
        axs[1].plot(self.df['atr'], color='red')
        plt.show()

    def graphing_williams_r(self):
        # Williams %R
        fig, axs = plt.subplots(2)
        axs[0].plot(self.df['Close'], color='green')
        axs[1].plot(self.df['williams r'], color='red')
        plt.axhline(y=-20, color='b', linestyle=':')
        plt.axhline(y=-80, color='b', linestyle=':')
        plt.show()



class Compile:
    prepare_data_obj = Prepare_data()

    def compile_analysis(self):
        global bb
        global roi
        global atr
        global will_r

        self.prepare_data_obj.retrive_dataset()
        self.prepare_data_obj.add_timestamp_df()

        if bb == 1:
            self.prepare_data_obj.bollinger_bands()
            self.prepare_data_obj.graphing_all_bb()
            print("BB")

        if roi == 1:
            self.prepare_data_obj.rate_of_change()
            self.prepare_data_obj.graphing_roi()
            print("ROI")

        if atr == 1:
            self.prepare_data_obj.average_true_range()
            self.prepare_data_obj.graphing_average_true_range()

        if will_r == 1:
            self.prepare_data_obj.williams_r()
            self.prepare_data_obj.graphing_williams_r()
