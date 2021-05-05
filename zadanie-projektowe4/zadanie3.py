
import numpy as np
import matplotlib.pyplot as plt
import random

arr_of_nums = []
numbers = []

for i in range(100):
    num = int(i)
    numbers.append(num)

for random_number in range(10000):
    number = int(random.randint(1,100));
    arr_of_nums.append(number)



plt.bar(courses, values)
plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")

plt.show()