valor_emprestimo = float(input("Informe o valor do empréstimo: "))
num_parcelas = int(input("Informe o número de parcelas: "))
salario_solicitante = float(input("Informe o salário do solicitante: "))

valor_parcela = valor_emprestimo / num_parcelas

if valor_parcela <= salario_solicitante * 0.3:
    print("Empréstimo aprovado.")
else:
    print("Empréstimo não aprovado.")