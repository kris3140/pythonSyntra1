# Functie om rechts uit te lijnen

def RechtsUitlijnen(tekst, rechtermarge):
    aantal_spaties = rechtermarge - len(tekst)
    print((' '* aantal_spaties) + tekst)



RechtsUitlijnen("banaan", 70)
RechtsUitlijnen("nog een banaan", 70)
RechtsUitlijnen("2 Euro 30", 70)
RechtsUitlijnen("dit is een hele lange zin", 70)



# eigen oefening

fruit = 'banana'

def printWordUpsideDown(word):
    index = -1
    counter = 0
    while index >= -len(word):
        letter = word[index]
        print((" "* counter) + letter)
        index = index - 1
        counter = counter + 1


printWordUpsideDown(fruit)

print(' ')


counter = len(fruit)
for letter in fruit:
    print((" "* counter) + letter)
    counter = counter - 1


print(" ")



