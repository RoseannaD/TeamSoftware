import yfinance as yahooFinance
import pandas as pd
import sys

fTest = open('length.txt', 'w')
fTest.write('0')
fTest.close()

stockName=sys.argv[1]
startDate=sys.argv[2]
endDate=sys.argv[3]
intLength = 0
Length = ''
stringData = ''

yahooData = yahooFinance.download(stockName, startDate, endDate)
intLength = len(yahooData.index)
Length = str(intLength)

stringData = yahooData.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, min_rows=None, max_cols=None, show_dimensions=False, decimal='.', line_width=None)

fData = open('output.txt', 'w')
fData.write(stringData)
fData.close()

fLength = open('length.txt','w')
fLength.write(Length)
fData.close()

#insert exception handling shit here
