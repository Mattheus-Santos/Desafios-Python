#Exercício Python 47:Esse é um programa que mostre na tela todos os números pares que estão no intervalo entre números definidos pelo usuário.

print("Nesse programa você pode escolher dois números para saber quais números pares há entre eles.")
number_1 = int(input("Digite o primeiro número:"))
number_2 = int(input("Digite o segundo número:"))

if number_1 < number_2:
    print(f"Os números pares entre {number_1} e {number_2} são:")
    for i in range(number_1, number_2 + 1):
        if i % 2 == 0:
            print(i, end=" ")

else:
    print("ERROR!!! O PRIMEIRO NÚMERO DEVE SER MENOR QUE O SEGUNDO NÚMERO.")