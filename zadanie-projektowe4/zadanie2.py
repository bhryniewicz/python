import matplotlib.pyplot as plt
import numpy
import random

arr_of_nums = []
numbers = []

values_of_num = []

for i in range(100):
    num = int(i)
    numbers.append(num)

for random_number in range(10000):
    number = int(random.randint(1,100));
    arr_of_nums.append(number)

for x in numbers:
    values_of_num.append(arr_of_nums.count(x))

print(numbers)
print(values_of_num)

plt.bar(numbers, values_of_num)

plt.xlabel("liczby wystepujace")
plt.ylabel("ilosc wystepowania")

plt.show()