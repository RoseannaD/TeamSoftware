class parameters:
    # A variable for predicting 'forecast_out' days out into the future
    future_days = 30 # 'n=30' days

class DataSet:
    stock_name = None
    start_date = None
    end_date = None
    stock_data = None

    def get_data(self, stock_code):
        #parse current date in the right format
        #DataSet_Obj.end_date = input("Enter current date: ")
        #DataSet_Obj.end_date = parser.parse(DataSet_Obj.end_date)
        end_date = date.today()

        #minus 6 months from current date and convert to correct format
        start_date = end_date - dateutil.relativedelta.relativedelta(years=5)
        start_date = start_date.strftime("%Y-%m-%d")

        #convert current date to correct format
        end_date = (end_date.strftime("%Y-%m-%d"))

        # Retrieve stock data
        stock_data = yf.download(stock_code, start_date, end_date)

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
    lr_df = None
    svm_df = None
    lr_confidence = None
    svm_confidence = None
    lr_prediction = None
    svm_prediction = None

    df = dataSet_obj.get_data("MSFT") #HARDCODED; CHANGE
