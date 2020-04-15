anotherCompany = 1
hotelOrTransport = False
haveSharePrice = False
sharePrice = 0
haveNetIncome = False
netIncome = 0
havePreferDiv = False
preferDiv = 0
haveOutstandingShares = False
outstandingShares = 0
haveAssets = False
assets = 0
haveLiabilities = False
liabilities = 0
haveAnnualDiv = False
annualDiv = 0
haveAnnualRev = False
annualRev = 0
haveTotalDebt = False
totalDebt = 0
haveMinorityInterest = False
minorityInterest = 0 
haveTotalCash = False
totalCash = 0
haveRentalCosts = False
rentalCosts = 0
haveTaxes = False
taxes = 0
haveDepreciation = False
depreciation = 0
haveAmortisation = False
amortisation = 0
haveMarketCapital = False
marketCapital = 0
havePreferStock = False
preferStock = 0
haveTotalEquity = False
totalEquity = 0
#haveEquivEquityInvest = False
#EquivEquityInvest = 0
haveNonOperatingCash = False
nonOperatingCash = 0

inputChecker = 0
userInput = ""
typoChecker = 0

while (anotherCompany == 1):
        print("Please enter as much information as you can. The more information that you provide, the more multiples that can be calculated.")
        while (inputChecker == 0):
                userInput = input ("Is the company a hotel company?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        hotelOrTransport = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        hotelOrTransport = False
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                        continue
                typoChecker = 0
                while (typoChecker == 0):
                        userInput = input("Is what you entered correct? Please enter yes or no")
                        if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                                inputChecker = inputChecker + 1
                                typoChecker = typoChecker + 1
                        elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                                print("That's fine. Please try again")
                                inputChecker = 0
                                typoChecker = typoChecker + 11 
                        else:
                                print("Please make sure that you only enter yes or no")
        inputChecker = 0
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the current share price?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0): 
                                userInput = input("Please enter the current share price")
                                if (userInput.isdigit()):
                                        sharePrice = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveSharePrice = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveSharePrice = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        "Please only enter yes or no"
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's current net income?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0): 
                                userInput = input("Please enter the company's current net income")
                                if (userInput.isdigit()):
                                        netIncome = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveNetIncome = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveNetIncome = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        "Please only enter yes or no"
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's preferred dividends?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0): 
                                userInput = input("Please enter the preferred dividends")
                                if (userInput.isdigit()):
                                        preferDiv = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        havePreferDiv = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        havePreferDiv = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's total outstanding shares?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0): 
                                userInput = input("Please enter the company's total outstanding shares")
                                if (userInput.isdigit()):
                                        outstandingShares = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveOutstandingShares = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveOutstandingShares = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's current assets?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0): 
                                userInput = input("Please enter the company's current assets")
                                if (userInput.isdigit()):
                                        assets = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveAssets = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveAssets = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you have the company's total current liabilities?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's total current liabilities")
                                if (userInput.isdigit()):
                                        liabilities = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveLiabilities = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveLiabilities = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's annual dividends?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0): 
                                userInput = input("Please enter the company's annual dividends")
                                if (userInput.isdigit()):
                                        annualDiv = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveAnnualDiv = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveAnnualDiv = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        "Please only enter yes or no"
        inputChecker = 0
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's annual revenue?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's annual revenue")
                                if (userInput.isdigit()):
                                        annualRev = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveAnnualRev = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveAnnualRev = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's total debt?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's total debt")
                                if (userInput.isdigit()):
                                        totalDebt = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else :
                                        print("Please ensure that you only enter digits")
                        haveTotalDebt = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveTotalDebt = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        "Please only enter yes or no"
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's minority interest?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's minority interest")
                                if (userInput.isdigit()):
                                        minorityInterest = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else :
                                        print("Please ensure that you only enter digits")
                        haveMinorityInterest = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveMinorityInterest = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        "Please only enter yes or no"
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's total cash and cash equivelents?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's total cash and cash equivelents")
                                if (userInput.isdigit()):
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                        totalCash = int(userInput)
                                else :
                                        print("Please ensure that you only enter digits")
                        haveTotalCash = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveTotalCash = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's total taxes?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's total taxes")
                                if (userInput.isdigit()):
                                        taxes = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveTaxes = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveTaxes = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's preferred stock?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's preferred stock")
                                if (userInput.isdigit()):
                                        preferStock = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        havePreferStock = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        havePreferStock = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's total equity?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's total equity")
                                if (userInput.isdigit()):
                                        totalEquity = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else :
                                        print("Please ensure that you only enter digits")
                        haveTotalEquity = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveTotalEquity = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        

        
        while (inputChecker == 0):
                userInput = input ("Do you know the company's total non-operating cash?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the company's total non-operating cash")
                                if (userInput.isdigit()):
                                        nonOperatingCash = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else :
                                        print("Please ensure that you only enter digits")
                        haveNonOperatingCash = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveNonOperatingCash = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know to total depreciation?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the total depreciation")
                                if (userInput.isdigit()):
                                        depreciation = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else: 
                                        print("Please ensure that you only enter digits")
                        haveDepreciation = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveDepreciation = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                else:
                        print("Please only enter yes or no")
        inputChecker = 0
        
        
        while (inputChecker == 0):
                userInput = input ("Do you know the amortisation?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        while (inputChecker == 0 ):
                                userInput = input("Please enter the amortisation")
                                if (userInput.isdigit()):
                                        amortisation = int(userInput)
                                        inputChecker = inputChecker + 1
                                        typoChecker = typoChecker + 1
                                else :
                                        print("Please ensure that you only enter digits")
                        haveAmortisation = True
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        haveAmortisation = False
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 1
                else:
                        print("There has been an error. Please ensure that you only enter either yes or no")
                
        typoChecker = 0
        while (typoChecker == 0):
                userInput = input("Is what you entered correct?")
                if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                        inputChecker = inputChecker + 1
                        typoChecker = typoChecker + 11
                elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                        print("Please try again")
                        typoChecker = typoChecker + 11
                        
                else:
                        print("Please only enter yes or no")
        inputChecker = 0       
        
        
        if (hotelOrTransport == True):
                while (inputChecker == 0):
                        userInput = input ("Do you know the total rental costs?")
                        if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                                while (inputChecker == 0 ):
                                        userInput = input("Please enter the total rental costs")
                                        if (userInput.isdigit()):
                                                rentalCosts = int(userInput)
                                                inputChecker = inputChecker + 1
                                                typoChecker = typoChecker + 1
                                        else :
                                                print("Please ensure that you only enter digits")
                                haveRentalCosts = True
                        elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                                haveRentalCosts = False
                                inputChecker = inputChecker + 1
                                typoChecker = typoChecker + 1
                        else:
                                print("There has been an error. Please ensure that you only enter either yes or no")
                
                typoChecker = 0
                while (typoChecker == 0):
                        userInput = input("Is what you entered correct?")
                        if (userInput == "Yes" or userInput == "yes" or userInput == "YES" or userInput == "y" or userInput == "Y"):
                                inputChecker = inputChecker + 1
                                typoChecker = typoChecker + 11
                        elif (userInput == "No" or userInput == "no" or userInput == "NO" or userInput == "n" or userInput == "N"):
                                print("Please try again")
                                typoChecker = typoChecker + 11
                        else:
                                print("Please only enter yes or no")
        inputChecker = 0
        
        
#Earnings Per Share Calculation
        earningsPerShare = 0
        haveEarningsPerShare = False
        if (haveNetIncome == True and haveOutstandingShares == True):
                haveEarningsPerShare = True
                earningsPerShare = netIncome / outstandingShares
        else:
                haveEarningsPerShare = False
        
#P/E Ratio
        PEratio = 0
        if (haveEarningsPerShare == True and haveSharePrice == True):
                PEratio = sharePrice / earningsPerShare
                print("P/E Ratio - ", PEratio)
        else:
                print("P/E Ratio - N/A")
        
#Book price calculation
        bookPrice = 0
        haveBookPrice = False
        if (haveAssets and haveLiabilities):
                haveBookPrice = True
                bookPrice = assets - liabilities
        
#Price/Book Ratio
        priceBookRatio = 0
        if (haveBookPrice == True and haveSharePrice == True):
                priceBookRatio = sharePrice / bookPrice
                print("Price/Book Ratio - " ,priceBookRatio)
        else:
                print("Price/Book Ratio - N/A")
                
#Dividend Yield
        diviYield = 0
        if (haveAnnualDiv == True and haveSharePrice == True):
                diviYield = annualDiv / sharePrice
                print("Dividend Yield - " ,diviYield)
        else:
                print("Dividend Yield - N/A")
        
#calculate market capital
        if (haveOutstandingShares == True and haveSharePrice):
                haveMarketCapital = True
                marketCapital = outstandingShares * sharePrice
        else:
                haveMarketCapital = False
        
#Price/Sales
        priceSales = 0 
        if (haveMarketCapital == True and haveAnnualRev == True):
                priceSales = marketCapital / annualRev
                print("Sales/Price Ratio - ", priceSales)
        else:
                print("Sales/Price Ratio - N/A")

#EV Calculation
        haveEnterValue = False
        enterValue = 0
        if (haveMarketCapital == True and havePreferStock == True and haveTotalDebt == True and haveMinorityInterest == True and haveTotalCash == True):
                haveEnterValue = True
                enterValue = marketCapital + preferStock + totalDebt + minorityInterest - totalCash
        else:
                haveEnterValue = False


#EV/Revenue
        EVrevenue = 0
        if (haveEnterValue == True and haveAnnualRev == True):
                EVrevenue = enterValue / annualRev
                print("EV/Revenue - " ,EVrevenue)
        else:
                print("EV/Revenue - N/A")
                
#EV/EBITDAR
        EBITDAR = 0
        EVebitdar = 0
        haveEBITDAR = False
        if (haveNetIncome == True and haveMinorityInterest == True and haveTaxes == True and haveDepreciation == True and haveAmortisation == True and haveRentalCosts == True):
                haveEBITDAR = True
                EBITDAR = netIncome + minorityInterest + taxes + depreciation + amortisation + rentalCosts
        else:
                haveEBITDAR = False
                print("EV/EBITDAR - N/A")
                
        if (haveEBITDAR == True and haveEnterValue == True):
                EVebitdar = enterValue / EBITDAR
                print("EV/EBITDAR - " ,EVebitdar)
                
#EV/EBITDA
        EBITDA = 0
        EVebitda = 0
        haveEBITDA = False
        if (haveNetIncome == True and haveMinorityInterest == True and haveTaxes == True and haveDepreciation == True and haveAmortisation == True and hotelOrTransport == False):
                haveEBITDA = True
                EBITDA = netIncome + minorityInterest + taxes + depreciation + amortisation
        else:
                haveEBITDA = False
                print("EV/EBITDA - N/A")
        if (haveEBITDA == True and haveEnterValue == True):
                EVebitda = enterValue / EBITDA
                print("EV/EBITDA - ", EVebitda)

#EV/Invested Capital
