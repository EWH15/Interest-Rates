
# try.github.io

currencies = {                      #this is a dictionary
    'USD': 1,
    'EURO': 1.176,
    'GBP': 1.28,
    'AUD': 1.02
}

def isValidCurrency(currency):
    if currency in currencies:      #checking a key of a dictionary or array, is a conditional
        return True
    return False

def convertCurrency(originCurrency, targetCurrency, value):
    if not isValidCurrency(originCurrency) or not isValidCurrency(targetCurrency):
      return False

    origin = currencies[originCurrency]
    target = currencies[targetCurrency]
    
    return (origin / target) * value
    
# if the origin currency is either USD, GBP, EURO or AUD
# then calculate against all target currencies 

converted = convertCurrency('EURO', 'GBP', 100)

if not converted:
  print("Did not use accepted currency")

else:
    print(converted)
