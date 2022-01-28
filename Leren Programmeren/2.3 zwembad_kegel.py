import math

def bereken_inhoud(doorsnede_gr, doorsnede_kl, hoogte):
    str_gr = doorsnede_gr / 2
    str_kl = doorsnede_kl / 2
    inhoud = math.pi / 3 * hoogte * (str_gr**2 + str_gr*str_kl + str_kl**2)
    inhoud = inhoud * 1000     # omzetten naar liter : 1 m3 = 1000 l
    print(' ')
    print('De inhoud van het zwembad is %d liter' % inhoud)


bereken_inhoud(12, 8, 6)
