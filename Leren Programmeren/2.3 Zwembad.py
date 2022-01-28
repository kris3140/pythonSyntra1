import math

def bereken_inhoud(straal, hoogte):
    inhoud = straal*straal*math.pi*hoogte
    inhoud = inhoud * 1000     # omzetten naar liter : 1 m3 = 1000 l
    print('De inhoud van het zwembad is %d liter' % inhoud)


bereken_inhoud(1.5, 0.5)
bereken_inhoud(2, 0.6)
bereken_inhoud(2.75, 0.8)


