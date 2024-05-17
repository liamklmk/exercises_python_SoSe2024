def buchstaben_zählen(string):
    count = 0
    for element in string:
        if element.isalpha() == True:
            count += 1
    print(count)

buchstaben_zählen("Hallo, Berlin!")