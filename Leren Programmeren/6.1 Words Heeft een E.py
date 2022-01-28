# Print worden zonder e


def HeeftEenE(word):
    x = False
    for letter in word:
        if letter == "e":
            x = True
    return x

file = open('words.txt', 'rt')

for line in file:
    if HeeftEenE(line) == False:
        print(line.strip())




