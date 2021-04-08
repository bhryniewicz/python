import random
import numpy as np

numbers = []
userNumbers = []

for number in range(6):
    number = int(random.randint(1,49))
    numbers.append(number)

for userNumber in range(6):
    user = int(input('podaj liczbe od 1 do 49: '))
    userNumbers.append(user)

values = np.intersect1d(numbers, userNumbers)

print(f"trafione wartosci {values}")


