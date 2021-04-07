
x = int(input('podaj x: '))
y = int(input('podaj y: '))

if(x == 0 or y == 0):
    print('Punkt nie znajduej sie w zadnej cwiartce')
elif(x > 0 and y > 0):
    print("punkt znajduje sie w I cwiartce")
elif(x < 0 and y > 0):
    print('punkt znajduje sie w II cwiartce')
elif(x < 0 and y < 0):
    print('punkt znajduje sie w III cwiartce')
else:
    print('punkt znajduje sie w IV cwiartce')