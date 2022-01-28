def rijmt_op(word, rijm):
    aantal = len(rijm) + 1
    x = False
    if (word[-aantal:-1]) == rijm:
        x = True
    return x


file = open('words.txt', 'rt')

for line in file:
    if rijmt_op(line, 'full'):
        print(line.strip())


