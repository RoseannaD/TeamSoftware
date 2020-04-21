#Needs to use python 3.8, Needs yfinance libary pip installed to run
import yfinance as yahooFinance
import pandas as pd
import sys
import matplotlib.pyplot as plot
#this checks that the files are blank
fTest = open('length.txt', 'w')
fTest.write('0')
fTest.close()

#This is just making sure that the program doesn't break if incorrect data is inputted
#stockName=sys.argv[1]
#startDate=sys.argv[2]
#endDate=sys.argv[3]
stockName='XOM'
startDate='2017-08-01'
endDate='2017-12-31'
safe =0



data = startDate.split("-")


#this code, including following if statements checks that the input is valid
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
    

#This then grabs the data, outputting an error message if it cannot be done and a reason why
intLength = 0
Length = ''
stringData = ''
if (safe == 0):
    try:
        df = yahooFinance.download(stockName, startDate, endDate)
        intLength = len(df.index)
        Length = str(intLength)

        stringData = df.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, min_rows=None, max_cols=None, show_dimensions=False, decimal='.', line_width=None)

        fData = open('output.txt', 'w')
        fData.write(stringData)
        fData.close()

        fLength = open('length.txt','w')
        fLength.write(Length)
        fData.close()
        print('Completed')
    except:
        print("Company or date not valid")
else:
    print("Date not valid")


#This is the start of the fibonacci 

#This should plot the data
fig, ax = plot.subplots()
ax.plot(df.Close, color='black')


#This should get the min
#   grabbing the first from panda to get a start point
temp = 0
i = 0
minstrValue = str(df.iloc[[2],[3]])
minvaluetemp = minstrValue.split("  ")
while (i < len(minvaluetemp)):
    print("value is:",minvaluetemp[i],":")
    i = i + 1
minValue = float(minvaluetemp[17])

counter = 3

#   this updates minval to the actual min value
while (counter < intLength):
        tempstrValue = str(df.iloc[[counter],[3]])
        arraytemp = tempstrValue.split(" ")
        try:
            temps = str(arraytemp[28])
        except:
            print("Outside array length heaven knows why")
            
        if (not temps):
            print("for some reason theres a null symbol here and god knows why, if only it could maintain a set amount of spaces between each piece of data aka 1")
 
        else:
            if (temps[0].isdigit()):
                temps = temps.strip()
                print(":",temps,":")
            else:
                print("Just why are you here, why do you exist here ''")
                 
        if(temps ==" ''"):
            print("no, just no")
        else:
            if (temps.isdigit()):
                if (temps[0].isdigit()):
                    temp = float(temps)
                else:
                    print("gotcha fucker")
        
        if (minValue > temp):
            minValue = temp
        else:
            temp  = 10000000
        counter = counter + 1

#This should get the max
temp = 0
maxstrValue = str(df.iloc[[2],[3]])
maxvaluetemp = maxstrValue.split("  ")    
maxValue = float(maxvaluetemp[17])

counter = 3

while (counter < intLength):
    tempstrValue = str(df.iloc[[counter],[3]])
    arraytemp = tempstrValue.split(" ")
    try:
        temps = str(arraytemp[28])
    except:
        print("Outside array length heaven knows why")
        
    if (not temps):
        print("for some reason theres a null symbol here and god knows why, if only it could maintain a set amount of spaces between each piece of data aka 1")

    else:
        if (temps[0].isdigit()):
            temps = temps.strip()
            print(":",temps,":")
        else:
            print("Just why are you here, why do you exist here ''")
             
    if(temps ==" ''"):
        print("no, just no")
    else:
        if (temps.isdigit()):
            if (temps[0].isdigit()):
                temp = float(temps)
            else:
                print("gotcha fucker")
    
    if (maxValue < temp):
        maxValue = temp
    else:
        temp  = 0
    counter = counter + 1

#this calculates the fib levels
diff = maxValue - minValue
levelOne = maxValue - 0.236 * diff
levelTwo = maxValue - 0.382 * diff
levelThree = maxValue - 0.618 * diff

#this finishes up
print ("Level", "Price")
print ("0 ", maxValue)
print ("0.236", levelOne)       
print ("0.382", levelTwo)
print ("0.618", levelThree)
print ("1 ", minValue)

ax.axhspan(levelOne, minValue, alpha=0.4, color='red')
ax.axhspan(levelTwo, levelOne, alpha=0.5, color='green')
ax.axhspan(levelThree, levelTwo, alpha=0.5, color='blue')
ax.axhspan(maxValue, levelThree, alpha=0.5, color='brown')

plot.ylabel("Price")
plot.xlabel("Date")
plot.legend(loc=2)
plot.show()
