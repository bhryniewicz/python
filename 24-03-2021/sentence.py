sentence = input('Podaj zdanie z przecinkami: ')

if sentence.find(',') == -1:
    print('Zdanie miało zawierać przecinki')
    quit()

parts = sentence.split(',')

i = 0
while i < len(parts):
    parts[i] = f"{i}{parts[i]}"
    i+=1

print(','.join(parts))