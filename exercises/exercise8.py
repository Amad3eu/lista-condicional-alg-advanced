horas_trabalhadas = float(input("Informe o número de horas trabalhadas no mês: "))
salario_hora = float(input("Informe o salário por hora: "))

if horas_trabalhadas > 160:
    horas_extras = horas_trabalhadas - 160
    salario_total = (160 * salario_hora) + (horas_extras * salario_hora * 1.5)
else:
    salario_total = horas_trabalhadas * salario_hora

print(f"O salário total é de R$ {salario_total:.2f}.")
