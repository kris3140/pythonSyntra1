# Euclides : grootste gemene deler

print(' ')
print('Berekening van de grootste gemene deler van twee getallen:')
print(' ')



def euclides(g1, g2):
    while g1 != g2:
        if g1 > g2:
            g1 = g1 - g2     # g1 -= g2
        else:
            g2 = g2 - g1
    return g1


getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef nog een getal: "))
ggd = euclides(getal1, getal2)
print(' ')
print('De grootste gemene deler van %d en %d is %d ' % (getal1, getal2, ggd) )
