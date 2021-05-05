first_number = [9,6,7]
last_number = [2,5,6]

adding_last_ones = first_number[-1] + last_number[-1]

if(adding_last_ones > 10):
    adding_last_ones = adding_last_ones - 10
    adding_second_ones = first_number[-2] + last_number[-2] + 1
else:
    adding_second_ones = first_number[-2] + last_number[-2]

if(adding_second_ones > 10):
    adding_second_ones = adding_second_ones - 10
    adding_third_ones = first_number[-3] + last_number[-3] + 1
else:
    adding_third_ones = first_number[-3] + last_number[-3]



print(f'wynik to {adding_third_ones}{adding_second_ones}{adding_last_ones}')

import math

#sprawdzenie czy liczba i podział na tablice
def splitAndConvertString(inp):
    try:
        result = []
        for i in inp:
            result.append(int(i))
        return result
    except ValueError:
        print('Podaj liczbę')

first = splitAndConvertString(input('Podaj pierwszą liczbę: '))
second = splitAndConvertString(input('Podaj drugą liczbę: '))

#odwrocenie tablicy z liczbami
first.reverse()
second.reverse()

#uzupełnienie zerami na końcu do najdłuższej liczby
if len(first) > len(second):
    for i in range(len(first) - len(second)):
        second.append(0)
elif len(second) > len(first):
    for i in range(len(second) - len(first)):
        first.append(0)
index = 0
rest = 0
result = []

#samo dodawanie
while index < len(first):
    #dodanie 2 liczb
    partly = first[index] + second[index] + rest
    #wyciągnięcie liczby dziesiątek - jeśli taka jest
    rest = math.floor(partly / 10)
    #zapis do wyniku liczby jedności
    result.append(str(partly % 10))

    index += 1

#dodanie do wyniku liczby dziesiątek
if rest != 0:
    result.append(str(rest))

result.reverse()
print(f'Wynik to {"".join(result)}')