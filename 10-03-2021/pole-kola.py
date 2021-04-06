import math

number = input('Podaj liczbe')
promien = float(number)
wynik = round(pow(promien, 2) * math.pi, 2)
print("wynik to: {0}".format(wynik))