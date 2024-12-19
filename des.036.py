casa = int(input("Qual o valor da casa?:"))
salario = int(input("Qual seu salário?:"))
parcela = int(input("Quantos anos você quer pagar?:"))

valor_Parcela = casa / (parcela * 12)
salario2 = salario * 30 / 100

if valor_Parcela <= salario2:
    print("Espréstimo aprovado!")
else:
    print("Empréstimo negado!")