
"""
Code snippet used from Ishan Shah for displaying of data correctly
"""
from datetime import datetime
# To plot
import matplotlib.pyplot as plt
#To handle retriving the maximum and minimum stock from the Data Frame created
import pandas as pd
# To import stock prices
import fix_yahoo_finance as yf


stockName='COKE'
startDate='2006-08-01'
endDate='2017-12-31'
safe =0








#safe = 1
#while(safe == 1):
    #safe =0
    #print("Enter Company Name:")
    #stockName = cin.getline()
    #print("Enter start date (YYYY-MM-DD):")
    #startDate = cin.getline()
    #print("Enter end date (YYYY-MM-DD):")
    #startDate = cin.getline()


currentdate = str(datetime.date(datetime.now()))
currentsplit = currentdate.split("-")

curyear = int(currentsplit[0])
curmonth = int(currentsplit[1])
curday = int(currentsplit[2])

data = startDate.split("-")
#this code, including following if statements checks that the input is valid about the date
snum1 = int(data[1])
snum2 = int(data[2])
snum0 = int(data[0])



if (snum1 < 1 or snum1 > 12):
    safe = safe + 1
    
if (snum1 == 1 or snum1 == 3 or snum1 ==5 or snum1 == 7 or snum1 == 8 or snum1 == 10 or snum1 == 12):
    if (snum2 < 1 or snum2 > 31):
        safe = safe + 1
        
if (snum1 ==4 or snum1 == 6 or snum1==9 or snum1 ==11):
    if (snum2 < 1 or snum2 > 30):
        safe = safe + 1
if (snum1==2):
    if (snum2 < 1 or snum2 > 28):
        safe = safe + 1
        
if (snum0< 1997):
    safe = safe + 1

if (snum0 > curyear):
    safe = safe + 1
if (snum0 == curyear):
    if (curmonth < snum1):
        safe = safe + 1
    if (curmonth == snum1):
        if ((curday-1) < snum2):
            safe = safe + 1
        if ((curday-1) == snum2):
            print("Sorry data for today isn't avalible till tomorow.")
            safe = safe + 1


    
data = endDate.split("-")

enum1 = int(data[1])
enum2 = int(data[2])
enum0 = int(data[0])

if (enum1 < 1 or enum1 > 12):
    safe = safe + 1
    
if (enum1 == 1 or enum1 == 3 or enum1 ==5 or enum1 == 7 or enum1 == 8 or enum1 == 10 or enum1 == 12):
    if (enum2 < 1 or enum2 > 31):
        safe = safe + 1
        
if (enum1 ==4 or enum1 == 6 or enum1==9 or enum1 ==11):
    if (enum2 < 1 or enum2 > 30):
        safe = safe + 1
if (enum1==2):
    if (enum2 < 1 or enum2 > 28):
        safe = safe + 1
        
if (enum0< 1997):
    safe = safe + 1

if (enum0 > curyear):
    safe = safe + 1
if (enum0 == curyear):
    if (curmonth < enum1):
        safe = safe + 1
    if (curmonth == enum1):
        if ((curday-1) < enum2):
            safe = safe + 1
        if ((curday-1) == enum2):
            print("Sorry data for today isn't avalible till tomorow.")
            safe = safe + 1
#need a leap year check
if (enum0<snum0):
    safe = safe + 1
if (enum0==snum0):
    if(enum1<snum1):
        safe = safe + 1
    if(enum1 == snum1):
        if(enum3 <= snum3):
            safe = safe + 1

    
if (safe == 0):
    
    try:
        df = yf.download(stockName,startDate,endDate)
           
    except:
        safe = safe + 1
        print("Company not valid - Function Crashed")
#end while
if (safe == 0):
    fig, ax = plt.subplots()
    ax.plot(df.Close, color='black')
    # Define minimum and maximum price points
    minValue = df['Low'].min()
    maxValue = df['High'].max()
    
    

    # Fibonacci Levels
    diff = maxValue - minValue
    level1 = maxValue - 0.236 * diff
    level2 = maxValue - 0.382 * diff
    level3 = maxValue - 0.618 * diff

    # Plot the price series
    print ("Level", "Stock")
    print ("0 ", maxValue)
    print ("0.236", level1)
    print ("0.382", level2)
    print ("0.618", level3)
    print ("1 ", minValue)

    ax.axhspan(level1, minValue, alpha=0.4, color='lightsalmon')
    ax.axhspan(level2, level1, alpha=0.5, color='palegoldenrod')
    ax.axhspan(level3, level2, alpha=0.5, color='palegreen')
    ax.axhspan(maxValue, level3, alpha=0.5, color='powderblue')

    plt.ylabel("Stock")
    plt.xlabel("Date")
    plt.legend(loc=2)
    plt.show()

              
