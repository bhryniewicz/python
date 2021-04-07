def potegi(a,b):
    if b == 0:
        return 1
    return a * potegi(a,b - 1)


print(potegi(2, 3))