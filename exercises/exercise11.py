import math

a = float(input("Informe o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau.")
else:
    b = float(input("Informe o valor de b: "))
    c = float(input("Informe o valor de c: "))

    delta = b**2 - 4 * a * c

    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")
