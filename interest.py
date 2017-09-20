#Mortage Rates

Banks = {
    'BOA': .0350,
    'Citi': .0375
}

Terms = {
    'Term1': 15,
    'Term2': 20,
    'Term3': 30
}

def IsValidBank(bank):
    if bank in Banks:
        return True
    else:
        return False

def IsValidTerm(term):
    if term in Terms:
        return True
    else:
        return False

def convertMonthlyInterestAmount(rate, month, amount):
    if not IsValidBank(rate) or not IsValidTerm(month):
        return False
    # (Banks[rate] / Terms[month]) * amount


    if rate == 'BOA' and month == 'Term1':
        return (Banks['BOA'] / Terms['Term1']) * amount
    elif rate == 'BOA' and month == 'Term2':
        return (Banks['BOA'] / Terms['Term2']) * amount
    elif rate == 'BOA' and month == 'Term3':
        return (Banks['BOA'] / Terms['Term3']) * amount
    elif rate == 'Citi' and month == 'Term1':
        return (Banks['Citi'] / Terms['Term1']) * amount
    elif rate == 'Citi' and month == 'Term2':
        return (Banks['Citi'] / Terms['Term2']) * amount
    elif rate == 'Citi' and month == 'Term3':
        return (Banks['Citi'] / Terms['Term3']) * amount
    else:
        return False



converted =  convertMonthlyInterestAmount('BOA', 'Term1', 200000)
if (converted):
    print "BOA monthly mortage amounts:"
    print converted
else:
    print "You did not choose a bank with a Mortgage rate"