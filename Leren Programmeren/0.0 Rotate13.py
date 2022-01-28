# program to rotate

# create a list for each type of character 0-9, A-Z, a-z
num_list = []
for i in range(48, 58): num_list.append(chr(i))
lower_list = []
for i in range(97, 123): lower_list.append(chr(i))
upper_list = []
for i in range(65, 91): upper_list.append(chr(i))


def encode_rotate(text, number):
    # find each character in one of the lists and check the index
    mylist = []
    mystring = ''
    for letter in text:
        if letter == ' ':
            mylist.append(letter)
            continue
        elif upper_list.count(letter) == 1:
            index = upper_list.index(letter)
            list_found = upper_list
        elif lower_list.count(letter) == 1:
            index = lower_list.index(letter)
            list_found = lower_list
        elif num_list.count(letter) == 1:
            index = num_list.index(letter)
            list_found = num_list
        else:
            mylist.append(letter)
            continue
        # add number to the index and if index exceeds length of list, correct the index
        index += number
        while index >= len(list_found):
            index -= len(list_found)
        mylist.append(list_found[index])
    # transform mylist into a string (we use a list because the append method does not exist for a string)
    for element in mylist:
        mystring += element
    return mystring


def decode_rotate(text, number):
    # find each character in one of the lists and check the index
    mylist = []
    mystring = ''
    for letter in text:
        if letter == ' ':
            mylist.append(letter)
            continue
        elif upper_list.count(letter) == 1:
            index = upper_list.index(letter)
            list_found = upper_list
        elif lower_list.count(letter) == 1:
            index = lower_list.index(letter)
            list_found = lower_list
        elif num_list.count(letter) == 1:
            index = num_list.index(letter)
            list_found = num_list
        else:
            mylist.append(letter)
            continue
        # deduct number from the index and if index exceeds length of list, correct the index
        index -= number
        while index >= len(list_found):
            index -= len(list_found)
        # add the new letter to mylist
        mylist.append(list_found[index])
    # transform mylist into a string (we use a list because the append method does not exist for a string)
    for element in mylist:
        mystring += element
    return mystring


# tekst = encode_rotate('Dit is een tekst, met speciale <> tekens.', -1)
tekst = decode_rotate('Chs hr ddm sdjrs, lds rodbhzkd <> sdjdmr.', -1)

print('tekst: ', tekst)



