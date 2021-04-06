source = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

try:
    sublistCount = int(input('Podaj długość podlisty: '))
except ValueError:
    print('Wartość powinna być liczbą całkowitą')
    quit()

if sublistCount <= 0:
    print('Wartość powinna być liczbą dodatnią')
    quit()

result = []

for i in range(sublistCount):
    print(source[i::sublistCount])
    result.append(source[i::sublistCount])

print(result)