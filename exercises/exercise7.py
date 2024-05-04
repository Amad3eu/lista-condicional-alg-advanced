nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado.")
elif 5 <= media < 7:
    print("Em exame.")
    nota_exame = float(input("Informe a nota do exame: "))
    nova_media = (media + nota_exame) / 2
    if nova_media >= 5:
        print("Aprovado no exame.")
    else:
        print("Reprovado no exame.")
else:
    print("Reprovado.")
