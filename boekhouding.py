# Import helper
from helper import *

# Import presentatie
from presentatie import *

import csv



# Dictionary
inkomsten = {
    "Aardbeien-ijs-totaal\t" : 1000,
    "Vanille-ijs-totaal\t"   : 2000,
    "Chocolade-ijs-totaal\t" : 1500,
    "Waterijsjes-totaal\t"   : 750 
}

# Totaal
totaal_inkomsten = som(inkomsten)

print()
print(totaal_inkomsten)
print()

# Presenteer totaal
presenteer(inkomsten, totaal_inkomsten)

# CSV
with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile,delimiter=';')
        writer.writerow([key,value])

