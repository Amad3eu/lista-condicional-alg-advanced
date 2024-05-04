nome_corretor = input("Informe o nome do corretor: ")
valor_venda = float(input("Informe o valor da venda: "))

if valor_venda > 50000:
    comissao = valor_venda * 0.12
elif 30000 <= valor_venda <= 50000:
    comissao = valor_venda * 0.095
else:
    comissao = valor_venda * 0.07

print(f"A comissão do corretor {nome_corretor} é de R$ {comissao:.2f}.")
