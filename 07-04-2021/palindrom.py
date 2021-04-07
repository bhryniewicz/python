def palindrome(string):
    if(string == string[::-1]):
        print('slowo jest palindormem')
    else:
        print('slowo nie jest palindromem')

word = input('podaj slowo: ')

palindrome(word)