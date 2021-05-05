numbers = [2,1,5,3,6,7,0,7]
len_of_arr = len(numbers)
sortedNumbers = []
for i in range(len_of_arr -1):
    if numbers[i] > numbers[i + 1]:
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

numbers.reverse()
print(numbers)