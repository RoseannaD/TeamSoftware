#Needs to use python 3.8, Needs yfinance libary pip installed to run
import yfinance as yahooFinance
import pandas as pd
import sys

fTest = open('length.txt', 'w')
fTest.write('0')
fTest.close()

#stockName=sys.argv[1]
#startDate=sys.argv[2]
#endDate=sys.argv[3]
stockName='Ford'
startDate='2003-01-13'
startmonthdays='-01-13'
startyear=2019
endDate='2019-06-01'
safe =0

data = startDate.split("-")

num1 = int(data[1])
num2 = int(data[2])
num0 = int(data[0])

if (num1 < 1 or num1 > 12):
    safe = safe + 1
    
if (num1 == 1 or num1 == 3 or num1 ==5 or num1 == 7 or num1 == 8 or num1 == 10 or num1 == 12):
    if (num2 < 1 or num2 > 31):
        safe = safe + 1
        
if (num1 ==4 or num1 == 6 or num1==9 or num1 ==11):
    if (num2 < 1 or num2 > 30):
        safe = safe + 1
if (num1==2):
    if (num2 < 1 or num2 > 28):
        safe = safe + 1
        
if (num0 >2020 or num0< 1997):
    safe = safe + 1
    
data = endDate.split("-")

num1 = int(data[1])
num2 = int(data[2])
num0 = int(data[0])

if (num1 < 1 or num1 > 12):
    safe = safe + 1
    
if (num1 == 1 or num1 == 3 or num1 ==5 or num1 == 7 or num1 == 8 or num1 == 10 or num1 == 12):
    if (num2 < 1 or num2 > 31):
        safe = safe + 1
        
if (num1 ==4 or num1 == 6 or num1==9 or num1 ==11):
    if (num2 < 1 or num2 > 30):
        safe = safe + 1
if (num1==2):
    if (num2 < 1 or num2 > 28):
        safe = safe + 1
        
if (num0 >2020 or num0< 1997):
    safe = safe + 1
    


intLength = 0
Length = ''
stringData = ''


df = yahooFinance.download(stockName, startDate, endDate)
intLength = len(df)
print("intLength:",intLength,":")
Length = str(intLength)

stringData = df.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, min_rows=None, max_cols=None, show_dimensions=False, decimal='.', line_width=None)

fData = open('output.txt', 'w')
fData.write(stringData)
fData.close()

fLength = open('length.txt','w')
fLength.write(Length)
fData.close()
print('Completed')

print("safe:",safe,":")
#calculating the moving average
#	first we need to assertain how many years the person want's the moving average for
inputCheck = 0
years = 0
dataexist = 0

try:
    test = df
except:
    dataexist =  dataexist + 1 

if (dataexist == 0):

    while (inputCheck == 0):
            yearInput = input("Please enter the number of years you want to calculate a moving average for: ")
            if (yearInput.isdigit()):
                    inputCheck = 1
            else:
                    print("Please ensure that you only enter numbers")

    years = int(yearInput)
    startyear = startyear - years
    endDate = str(startyear)+startmonthdays #only get the data for the selected time

    df = yahooFinance.download(stockName, startDate, endDate)
    #	giving user options of what sort of moving average they would like
    inputCheck = 0
    optionInput = ""
    while (inputCheck == 0): 
            print("Which of the following moving averages would you like to calculate?")
            print("A - Simple Moving Average")
            print("B - Exponentail Moving Average")
            print("C - Both of the above")
            optionInput = input("Please enter either A, B or C only")
            if (optionInput == "A" or optionInput == "B" or optionInput == "C" or optionInput == "a" or optionInput == "b" or optionInput == "c"):
                    inputCheck = 1
            else:
                    print("Invalid input detected! Please try again")

    # this is where we perform the maths on the moving average
    #	calculating simple moving average
    if (optionInput == "A" or optionInput == "a"):
            #working out how many values we need to get
            
            #this works out the first number we need 
            
            adder = df['Close'].sum()
            numValues = len(df.index)
            #this does the math and then outputs
            
                    
            simpleMovingAverage = adder / numValues
            print("The simple moving average is ", simpleMovingAverage)

    #	calculating Exponential moving average	
    elif (optionInput == "B" or optionInput == "b"):
            #to calculate exponetial moving average, you need to work with weighting and factorials as that is the best way to get even weighting over time
            counter = 1
            factorial = 1
            
            #this calculates the weighting
            while (counter <= (years*365)):
                    factorial = factorial * counter
                    counter = counter + 1
            
            weight = 1
            counter = 1
            tempAverage = 0
            datavalues = df[['Close']]
            df['count'] = range(1, len(df) + 1)
            df.set_index('count', drop=False, append=False, inplace=True, verify_integrity=False)
            
            counter = len(df.index)
            farback = len(df.index)-(years * 365)
            #doing the actual mathy bit
            while (counter >= farback):
                    
                    print(weight / factorial)
                    tempAverage = tempAverage + df.at[counter, 'Close'] * complex((weight /factorial))
                    print(tempAverage)
                    tadah= input("Space")
                    counter = counter - 1 
                    weight = weight + 1
            print("The exponential moving average is ", tempAverage)
            
    elif (optionInput == "C" or optionInput == "c"):
            #basically just copying my own two code sections from above and mashing together
            # 	Simple Moving Average
            adder = df['Close'].sum()
            numValues = len(df.index)
            #this does the math and then outputs
            
                    
            simpleMovingAverage = adder / numValues
            print("The simple moving average is ", simpleMovingAverage)
            
            #	Exponential Moving Average
            counter = 1
            factorial = 1
            
            #this calculates the weighting
            while (counter <= (years*365)):
                    factorial = factorial * counter
                    counter = counter + 1
            
            weight = 1
            counter = 1
            tempAverage = 0
            datavalues = df[['Close']]
            df['count'] = range(1, len(df) + 1)
            df.set_index('count', drop=False, append=False, inplace=True, verify_integrity=False)
            
            counter = len(df.index)
            farback = len(df.index)-(years * 365)
            #doing the actual mathy bit
            while (counter >= farback):
                    
                    print(weight / factorial)
                    tempAverage = tempAverage + df.at[counter, 'Close'] * complex((weight /factorial))
                    print(tempAverage)
                    tadah= input("Space")
                    counter = counter - 1 
                    weight = weight + 1
            print("The exponential moving average is ", tempAverage)
            
    else: 
            print("There has been an unexpected error, please try again")
else:
    print("Incorrect symbol for stock")
