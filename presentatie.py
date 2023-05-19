# Presenteer
def presenteer(mijn_dict, totaal):
    for sleutel, waarde in mijn_dict.items():
        print(f"{sleutel} : {waarde} euro")
    print("====================================")
    print(f"totaal : {totaal} euro")


mijn_dict = {
    'vis'   : 10, 
    'vlees' : 25, 
    'overig': 15
}
totaal = 50

# print()
# presenteer(mijn_dict, totaal)