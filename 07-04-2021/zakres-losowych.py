import random

def randomNumbers(liczba ,start, koniec):
    for x in range(liczba):
        x = int(random.randint(start, koniec))
        print(x)

a = int(input('podaj ilosc liczb do wyswietlenia: '))
b = int(input('podaj liczbe poczatkowa: '))
c = int(input('podaj ilosc koncowa: '))

randomNumbers(a, b, c)