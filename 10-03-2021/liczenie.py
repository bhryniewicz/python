import math

a = input('podaj szerokosc')
b = input('podaj wysokosc')
anum = float(a)
bnum = float(b)
if anum < 0 or bnum < 0 :
    print('zle wymiary')
else :
    pole = anum * bnum
    obw = 2 * anum + 2 * bnum
    przekatna = pow(pow(anum, 2) + pow(bnum, 2), 0.5)


print(f"Pole to: {pole}")
print(f"Obwod to: {obw}")
print(f"Przekatna to: {przekatna}")