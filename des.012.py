salario = float(input("Qual seu salário atual?"))
aumento = float(input("Qual a porcentagem de aumento do salário?"))
novo_salario = salario + (salario * aumento / 100)
print("Seu salário é:{:.2f} e com um aumento de {:.2f}% passa a ser de:{:.2f}!".format(salario, aumento, novo_salario))