samogloski = ['a', 'o', 'u', 'i', 'y', 'e']

zdanie = input('podaj zdanie')

for letter in samogloski:
    zdanie = zdanie.replace(letter, letter.upper())
print(zdanie)xxxxxxx