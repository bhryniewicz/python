file = open('./projektowe.txt', 'r')

#jezeli liczymy odjecie spacji
#jezeli z to bez replace()

data = file.read().replace(" ","")

alphabet = 'abcdefghijklmnoprstuwxyzqvABCDEFGHIJKLMNOPRSTUWXYZQV'

for letter in alphabet:
    print(f'litera {letter}: {data.count(letter)}')


print(f'Liczba liter: {len(data)}')
