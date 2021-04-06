import random

number = random.randint(1, 100)

print(number)

if number % 2 == 0:
    print("Parzysta")
else:
    print("nieparzysta")
if number % 3 == 0:
    print("podzielna przez 3")
else:
    print("niepodzielna przez 3")