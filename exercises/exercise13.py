litros = float(input("Informe o número de litros vendidos: "))
combustivel = input("Informe o tipo de combustível (A-álcool, G-gasolina): ")

preco_gasolina = 3.30
preco_alcool = 2.90

if combustivel.upper() == "A":
    if litros <= 20:
        valor = litros * preco_alcool * (1 - 0.03)
    else:
        valor = litros * preco_alcool * (1 - 0.05)
elif combustivel.upper() == "G":
    if litros <= 20:
        valor = litros * preco_gasolina * (1 - 0.04)
    else:
        valor = litros * preco_gasolina * (1 - 0.06)

print(f"O valor a ser pago pelo cliente é R$ {valor:.2f}.")