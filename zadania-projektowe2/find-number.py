import random

number = int(random.randint(1,100))
print(number)

count = 0
chosenNumber = int(input("Jaka to liczba? "))
count += 1

while chosenNumber != number:
    chosenNumber = int(input("Jaka to liczba? "))
    if chosenNumber > number: 
        print(f'Liczba {chosenNumber} jest większa od szukanej')
    else:
        print(f'Liczba {chosenNumber} jest mniejsza od szukanej')
    count += 1

print(f'Znalazles liczbe po {count} razach')