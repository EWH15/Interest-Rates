#Mortage Rates

banks = {
    'BOA': .0350,
    'CITI': .0375
}

terms = {
    'Term1': 15,
    'Term2': 20,
    'Term3': 30
}

def IsValidBank(bank):              #this checks the validity of keys in banks
    if bank in banks:
        return True
    else:
        return False

def IsValidTerm(term):              #this checks the validity of the keys terms
    if term in terms:
        return True
    else:
        return False

def convertMonthlyInterestAmount(rate, month, amount):
    if not IsValidBank(rate) or not IsValidTerm(month):         #this is saying if IsValidBank and IsValidTerm are not valid, do not
        return False                                            #run, but if true run the calc
    
    return (banks[rate] / terms[month]) * amount                #replaces using if else statement to shorten the program


def convertedMontlyInterestAmounts(rate, month, value)
    
    #create dictionaries to run all iterations through
    bankRates = {}
    termLength = {}

    






converted =  convertMonthlyInterestAmount('CITI', 'Term1', 200000)       #calc to again shorten the process and also print out the result
                                                                        #also print out a statement if false
if (converted):
    print converted
else:
    print "You did not choose a bank with a Mortgage rate, please choose again."