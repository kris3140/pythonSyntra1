# berekenen percentages verkiezingsuitslagen


def rechts_uitlijnen(tekst, rechtermarge):
    aantal_spaties = rechtermarge - len(tekst)
    print((' '* aantal_spaties) + tekst)


def links_uitlijnen(tekst, linkermarge):
    aantal_spaties = linkermarge - len(tekst)
    print( tekst + (' ' * aantal_spaties), end='')

stemmen =	{
"NVA": 2455,
"SP-A": 2856,
"CD&V": 1501,
"GROEN": 1744,
"OPEN-VLD": 1988,
"VLAAMSBELANG": 586,
"PVDA": 697
}

totaal = 0
for aantal_stemmen in stemmen.values():
    totaal += aantal_stemmen
else:
    print('Totaal aantal stemmen: ', totaal )


print(' ')
totaal_perc = 0
for partij, aantal_stemmen in stemmen.items():
    links_uitlijnen(partij, 35)
    percent = format((aantal_stemmen / totaal * 100), ".2f")
    rechts_uitlijnen(str(percent), 5)
    totaal_perc += float(percent)


print(' ')
links_uitlijnen('Totaal van de percentages:  ', 35)
rechts_uitlijnen(str(totaal_perc), 5)


