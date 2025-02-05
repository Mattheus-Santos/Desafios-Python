#Esse programa um menu na qual os usuário pode escolher entre 5 opções: somar, multiplicar, maior, novos números e sair.
print(f"-------PROGRAMA CÁLCULOS-------")
opção = 0
num1 = int(input(f"Digite um número: "))
num2 = int(input(f"Digite outro número: "))
while opção != 5:

    print(f"[1] SOMAR")
    print(f"[2] MULTIPLICAR")
    print(f"[3] MAIOR")
    print(f"[4] NOVOS NÚMEROS")
    print(f"[5] SAIR")
    opção = int(input(f"Digite sua opção: "))
    if opção == 1:
        soma = num2 + num1
        print(f"A soma de {num1} e {num2} é {soma}.")
        print(f"===========================================")
    if opção == 2:
        mult = num1 * num2
        print(f"O número {num1} multiplicado por {num2} é igual a: {mult}.")
        print(f"===========================================")
    if opção == 3:
        if num1 > num2:
            print(f"O número {num1} é maior que {num2}.")
            print(f"===========================================")
        elif num2 > num1:
            print(f"O número {num2} é maior que {num1}.")
            print(f"===========================================")
        else:
            print(f"O número {num2} e {num1} são iguais.")
            print(f"===========================================")
    if opção == 4:
        num1 = int(input(f"Digite um número: "))
        num2 = int(input(f"Digite outro número: "))

    elif opção > 5 or opção < 1:
        print("OPÇÃO INVÁLIDA!!!")
        #break

print(f"PROGRAMA FINALIZADO.")