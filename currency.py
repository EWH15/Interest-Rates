
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

def convertCurrencies(originCurrency, value):
    conversions = {}
    
    # If given one currency, find all other currencies - Google: "Python get keys from dictionary" - should return a *List* of keys
    availableCurrencies = currencies.keys()
    # Run currency function on all the other currencies - Google: "Python: How to iterate a list" AKA: A for loop!
    for availableCurrency in availableCurrencies:
        if availableCurrency != originCurrency:
          conversions[availableCurrency] = convertCurrency(originCurrency, availableCurrency, value)
    # Return a dictionary of all converted

    return conversions


print(convertCurrencies('USD', 100))


# if the origin currency is either USD, GBP, EURO or AUD
# then calculate against all target currencies 

converted = convertCurrency('EURO', 'GBP', 100)

if not converted:
  print("Did not use accepted currency")

else:
    print(converted)
