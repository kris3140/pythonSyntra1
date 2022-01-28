


def Gemiddelde(lijst):
    som = 0
    for getal in lijst:
        som = som + getal
    avg = som / len(lijst)
    return avg



lijst = [14, 5, 8, 9, 13, 18, 16, 25]
G = Gemiddelde(lijst)
print('het gemiddelde is: ', G)

