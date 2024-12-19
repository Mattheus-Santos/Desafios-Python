numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite outro número:"))

if numero1 > numero2:
    print(f"O número {numero1} é maior que o número {numero2}.")
elif numero2 > numero1:
    print(f"O número {numero2} é maior que o número {numero1}")
else:
    print(f"Não existe valor maior, os dois números são iguais.")