lado1 = float(input("Informe o primeiro lado do triângulo: "))
lado2 = float(input("Informe o segundo lado do triângulo: "))
lado3 = float(input("Informe o terceiro lado do triângulo: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    if lado1 == lado2 == lado3:
        print("Triângulo equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Os lados informados não formam um triângulo.")
