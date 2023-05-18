# Sterrentitel
def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

# Fooienpot
def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag / personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"

# Onderstreping met ===
def onderstreep(tekst= ""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

# som
def som(dictionary):
    totaal = sum(dictionary.values())
    return totaal
