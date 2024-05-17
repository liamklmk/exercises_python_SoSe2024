import matplotlib.pyplot as plt

r = 0.5
a = 1
n = 10
summe = 0
s_n = []

for k in range(0, n):
        summe += a * r ** k
        s_n.append(summe)
        
print(s_n)
plt.plot(s_n)

#quad_zahlen = [zahlen if zahlen % 2 == 0 else zahlen ** 2 for zahlen in range(1, 11)]