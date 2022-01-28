def HeeftEenLetterUitLijst(word, list):
    x = False
    for letter in word:
        for letr in list:
            if letter == letr:
                x = True
    return x


file = open('words.txt', 'rt')

lijst1 = ["a", "e", "o"]
lijst2 = ["n", "s", "t", "v", "w"]

for line in file:
    if HeeftEenLetterUitLijst(line, lijst1) == False:
        print(line.strip())




