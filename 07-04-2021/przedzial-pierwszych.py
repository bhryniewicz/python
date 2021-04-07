def pierszwa(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def pierszwaPrzedzial(start, end):
    numbers = []
    for x in range(start, end + 1):
        if(pierszwa(x) == True):
            numbers.append(x)
    print(numbers)

a = int(input("podaj pierwsza liczbe z zakresu"))
b = int(input("podaj ostatnia liczbe z zakresu"))


pierszwaPrzedzial(a, b)