import random

def Deelbaar_Door(getal, deler):
    if (getal % deler) > 0:
        return False
    else:
        return True


for i in range(20):
    random_getal = random.randint(100, 999)
    y = 7
    if Deelbaar_Door(random_getal, y) == True:
        print('%d is deelbaar door %d' % (random_getal, y))
    else:
        print(random_getal)

