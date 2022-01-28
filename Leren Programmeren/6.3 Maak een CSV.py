
file = open('words.txt', 'rt')

vorige_eerste_letter = "a"
lijst = ''
print(lijst)
teller = 0
for word in file:
    if word[0] == vorige_eerste_letter:
        teller += 1
        if teller <= 5:
            lijst = lijst + (word.strip()) + ';'
        if teller == 5:
            lijst = lijst + '\n'
    else:
        teller = 1
        vorige_eerste_letter = word[0]
        lijst = lijst + (word.strip()) + ';'

f = open('CSVfile.text', "w")
f.write(lijst)
f.close()


