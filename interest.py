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

def convertMonthlyInterestAmount(bank, month, amount):
    if not IsValidBank(bank) or not IsValidTerm(month):         #this is saying if IsValidBank and IsValidTerm are not valid, do not
        return False                                            #run, but if true run the calc

    return (banks[bank] / terms[month]) * amount                #replaces using if else statement to shorten the program


def getAllTermRatesForBank(bank, amount):
  termKeys = terms.keys()
  rates = {}
  for term in termKeys:
      convertedInterest = convertMonthlyInterestAmount(bank, term, amount)
      if convertedInterest is not False:
        rates[term] = convertedInterest
  return rates

def getAllTermsForAllBanks(amount):
    bankKeys = banks.keys()
    allBanks = {}
    for bank in bankKeys:
        convertedBanks = getAllTermRatesForBank(bank, amount)
        if convertedBanks is not False:
          allBanks[bank] = convertedBanks
        
    return allBanks

print(getAllTermsForAllBanks(500000))


  

