from collections import OrderedDict

file = open('words.txt', 'rt')

vorige_eerste_letter = "a"
dict = {}
teller = 0
for word in file:
    if word[0] == vorige_eerste_letter:
        teller += 1
        dict[word[0]] = teller
    else:
        teller = 1
        vorige_eerste_letter = word[0]

sorted_dict = {}
sorted_dict = OrderedDict(sorted(dict.items(), key=lambda kv: kv[1], reverse=True))

for letter, aantal in sorted_dict.items():
    print(letter,':', aantal, '   ', end='')





