import math

n = input('podaj silnie')
n = float(n)
suma = 1
while n > 0:
    suma *= n
    n -= 1
print(suma)

