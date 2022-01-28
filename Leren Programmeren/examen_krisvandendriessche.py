# boodschappenlijstje

# functie om te aligneren
def align(tekst, breedte, modus):
    # we verminderen de breedte met de lengte van de tekst
    breedte -= int(len(str(tekst)))
    # aligneren linksv 'L' of rechts 'R'
    if modus == 'L':
        return (str(tekst) + " " * breedte)
    if modus == 'R':
        return (" " * breedte + str(tekst))


# functie om te printen
def KrisVandendriessche(dict):
    # initialisatie van variabelen
    aantal_lijnen = 0
    totaal_aantal = 0
    print()
    print('--------------- B O O D S C H A P P E N ---------------')
    # doorloop alle keys/value paren van het lijstje
    for artikel, aantal in dict.items():
        # call de align functie
        artikel_aligned = align(artikel, breedte=40, modus='L')
        aantal_aligned = align(aantal, breedte=15, modus='R')
        # print artikels en aantallen
        print(artikel_aligned, end='')
        print(aantal_aligned)
        # tel het aantal artikels en het totaal aantal
        aantal_lijnen += 1
        totaal_aantal += aantal
    print('-------------------------------------------------------')
    aantal_lijnen_aligned = align(('Aantal lijnen: ' + str(aantal_lijnen)), breedte=40, modus='L')
    print(aantal_lijnen_aligned, end='')
    totaal_aantal_aligned = align(('Totaal: ' + str(totaal_aantal)), breedte=15, modus='R')
    print(totaal_aantal_aligned)
    print('-------------------------------------------------------')




# initialisatie van variabelen
lijstje = {}
artikel = ''

# input aan de gebruiker vragen
while artikel != 'q':
    artikel = str(input("Welk artikel? "))
    if artikel != 'q':
        aantal = int(input("Aantal? "))
        # maak een item met key en value in de dictionary 'lijstje'
        lijstje[artikel.capitalize()] = aantal

#lijstje_sorted = sorted(lijstje.items(), key=lambda kv: kv[0], reverse=False)
#print(lijstje_sorted)

# function call om het lijstje te printen
KrisVandendriessche(lijstje)






