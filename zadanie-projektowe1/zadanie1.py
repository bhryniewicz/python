import math

suma = 0

first = float(input('podaj pierwsza liczbe z zakresu'))
last = float(input('podaj ostatnia liczbe z zakresu'))

while first != last + 1:
    suma += first
    first += 1
print(suma)

first1 = int(input('podaj pierwsza liczbe z zakresu'))
last1 = int(input('podaj ostatnia liczbe z zakresu'))

suma1 = 0

for x in range (first1,last1 + 1):
    suma1 += x
else:
    print(suma1)