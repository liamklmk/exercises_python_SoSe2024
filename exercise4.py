zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in zahlen:
    if x % 2 != 0:
        print(x**2)
    
    else:
        print(x)

quad_zahl = []

for x in zahlen:
    if x % 2 != 0:
        quad_zahl.append(x**2)
    
    else:
        quad_zahl.append(x)

print(quad_zahl)

quad_zahlen = [zahlen if zahlen % 2 == 0 else zahlen ** 2 for zahlen in range(1, 11)]

print(quad_zahlen)