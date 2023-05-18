from algemene_functies import mijn_functie_2

# Aanbieding
def aanbieding_1(smaak, prijs, korting):
    bedrag = prijs * korting
    korting = prijs - bedrag
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting} euro."

print()
print(aanbieding_1("aardbei", 4, 0.1 ))
print()

# Week inkomsten
def inkomsten_totaal(inkomsten, btw):
    inkomsten = sum(inkomsten)
    return f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."
    

inkomsten_dagelijks = [220, 430, 125, 160, 205, 90, 345]
btw = sum(inkomsten_dagelijks) / 100 * 21

print(inkomsten_totaal(inkomsten_dagelijks, btw))
print()

# Hoog en laag
def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]
    

print(laag_en_hoog(inkomsten_dagelijks))
print()

# Gemiddeld dag inkomen
def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    aantal = len(mijn_lijst)
    gemiddelde = som / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde} euro."

print(gemiddelde(inkomsten_dagelijks))
print()

# Meervoudig
def meervoudig(invoer_lijst):
    global laag_en_hoog
    return laag_en_hoog(invoer_lijst)

lijst = [10, 5, 3, 2, 1, 2, 9]

print(meervoudig(lijst))
print()

# Combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer

invoer_lijst_2 = [1, 2]

print(combinatie(invoer_lijst_2))
print()