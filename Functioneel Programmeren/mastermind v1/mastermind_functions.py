import random

def get_random(keuzeLijst):
    randomLijst = []
    for x in range(4):
        randomLijst.append(random.choice(keuzeLijst))
    print(randomLijst)
    return randomLijst

def get_input(lijst):
    gok = input('Doe een nieuwe gok: ')
    gok = gok.upper()
    gokLijst = [char for char in gok]
    if gok == 'STOP':
        print('Jammer, het juiste antwoord was:', lijst)
        return 'stop'
    else:
        return gokLijst

def check_juiste(aLijst, gLijst):
    aLijstCopy = aLijst.copy()
    gLijstCopy = gLijst.copy()
    juistePlaats = 0
    for x in range(4):
        if gLijst[x] == aLijst[x]:
            juistePlaats += 1
            gLijstCopy[x] = 'Y'
            aLijstCopy[x] = 'X'
            #print(aLijstCopy, gLijstCopy)
    if juistePlaats < 4:
        if juistePlaats == 1:
            print(juistePlaats, 'letter op de juiste plaats')
        else:
            print(juistePlaats, 'letters op de juiste plaats')
        return [aLijstCopy, gLijstCopy]
    else:
        print('Goed geraden !!')
        return 'alles geraden'

def check_foute(listsInList):
    aLijstCopy = listsInList[0]
    gLijstCopy = listsInList[1]
    foutePlaats = 0
    for antwoord in aLijstCopy:
        for gok in gLijstCopy:
            if gok == antwoord:
                #print(gok, antwoord)
                foutePlaats += 1
                gok = 'Y'
                antwoord = 'X'
                #print(aLijstCopy, gLijstCopy)
    if foutePlaats == 1:
        print(foutePlaats, 'letter op de foute plaats')
    else:
        print(foutePlaats, 'letters op de foute plaats')
