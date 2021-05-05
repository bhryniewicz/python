def draw_a_square(x, y, sign):
    for i in range(x):
        for i in range(y):
            print(sign, end = " ")
        print()

width = int(input('podaj szerokosc'))
height = int(input('podaj wysokosc'))
char = input('podaj znak ktorym bedzie rysowana figura')

draw_a_square(width,height, char)