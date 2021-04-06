import random

numbers = []

for number in range(1, 21):
    x = random.randint(1, 100)
    numbers.append(x)

print(numbers)

numbers.sort()

userNumber = int(input("Podaj liczbe: "))

for number in numbers:
    if number % userNumber == 0:
        print(f"{number}, ", end="")