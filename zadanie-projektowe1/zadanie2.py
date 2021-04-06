word = input('podaj slowo: ')


if len(word) < 8:
    print('za malo liter')
elif word.isalpha() == False:
    print('nie moze zawierac cyfr')
else: 
    print(f'Pierwsze 3 litery to: {word[0:3]}')
    print(f'Drugi znak od konca to: {word[-2]}')
    print(f'Ostatnie 4 znaki to: {word[-4:]}')
    print(f'Od 2 do przedostatniego w odwrotnej kolejnosci: {word[::-1]}')