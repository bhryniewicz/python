def n_value(a_1, r, n):
    if n <= 0:
        return 0
    a_n = a_1 + n_value(r, r, (n - 1)) 
    return a_n

first_n = int(input('podaj poczatkowy wyraz ciagu'))
r = int(input('podaj promień'))
numbers_of_n = int(input('który wyraz ciągu'))

print(n_value(first_n, r, numbers_of_n))