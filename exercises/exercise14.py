kg_strawberries = float(input("Insira a quantidade de morangos em Kg: "))
kg_apples = float(input("Insira a quantidade de maçãs em Kg: "))

if kg_strawberries <= 5:
    price_strawberries = 2.50
else:
    price_strawberries = 2.20

if kg_apples <= 5:
    price_apples = 1.80
else:
    price_apples = 1.50

total_cost = (kg_strawberries * price_strawberries) + (kg_apples * price_apples)

if kg_strawberries + kg_apples > 8 or total_cost > 25:
    total_cost *= 0.9

print(f"O custo total é: R$ {total_cost:.2f}")
