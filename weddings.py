#create a program that will calculate multiple variations of wedding venue costs (price per person, minimums)
#list of venues, list of photographers, list of florists, list of djs

venues = {
        'Ryland Inn': 33000,
        'Falkirk': 27000,
        'The Old Field Club': 25000,
        'Perona Farms': 32000,
        'The Whitby': 28000
    }

djs = {
    'Scratch Weddings': 1500,
    'The DJ': 2000,
    'Hank Lane': 2500
}

photographers = {
    'Jen Larsen': 4900,
    'Bri Johnson': 5100,
    'Debbie': 4800,
    'Lauren': 5000
}

florists = {
    'Florist1': 4500,
    'Florist2': 4000,
    'Florist3': 3500
}

def validVenues(venue):
    if venue in venues:
        return True
    else:
        return False

def validDjs(dj):
    if dj in djs:
        return True
    else:
        return False

def validPhotographers(photographer):
    if photographer in photographers:
        return True
    else:
        return False

def validFlorists(florist):
    if florist in florists:
        return True
    else:
        return False

def totalCost(venue, dj, photo, florist):
    if not validVenues or not validDjs or not validPhotographers or not validFlorists:
        return False
    return venues[venue] + djs[dj] + photographers[photo] + florists[florist]

print totalCost('Falkirk', 'Scratch Weddings', 'Jen Larsen', 'Florist1')