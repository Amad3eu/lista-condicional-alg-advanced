num_apples = int(input("Digite o número de maçãs compradas: "))
if num_apples < 12:
    cost = num_apples * 1.30
else:
    cost = num_apples * 1.00
print("O custo total da compra é: R$", cost)
