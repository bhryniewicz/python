import random

a = int(random.randint(1, 10))
b = int(random.randint(1, 10))

print(f"a: {a}, b: {b}")

suma = int(input("Podaj ich sume: "))

if (a + b) == suma:
    print("dobrze policzyle")
else:
    print("zle policzyles")