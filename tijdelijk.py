from helper import decoreer

# Dictionary
def print_aanbieding():
    prijzen = { 
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    # Variabele voor waarde element vanille
    aanbieding = prijzen["aardbei"] * 0.8

    # Teksten
    reclame_tekst  = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € + {aanbieding}"
    reclame_tekst2 = reclame_tekst[:-14]
    reclame_tekst3 = reclame_tekst2.upper()
    reclame_tekst4 = reclame_tekst3.split()

    # Loop en output
    for el in reclame_tekst4:
        if  len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

decoreer("Aanbieding")
print_aanbieding()