salario_atual = float(input("Informe o salário atual do funcionário: "))
salario_minimo = float(input("Informe o valor do salário mínimo: "))

if salario_atual < 3 * salario_minimo:
    reajuste = 0.50
elif 3 * salario_minimo <= salario_atual <= 10 * salario_minimo:
    reajuste = 0.20
elif 10 * salario_minimo < salario_atual <= 20 * salario_minimo:
    reajuste = 0.15
else:
    reajuste = 0.10

novo_salario = salario_atual + (salario_atual * reajuste)

print(f"O novo salário é de R$ {novo_salario:.2f}.")
