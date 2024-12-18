salario = int(input("Qual o salário do funcionário?:"))

if salario > 1250:
    aumento = (salario * 10 / 100) + salario
    print(f"Seu novo salário com aumento é:{aumento}")
else:
    aumento = (salario * 15 / 100) + salario
    print(f"Seu novo salário com aumento é:{aumento}")
