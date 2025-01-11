#Programa de uma tabuada de multiplicar.

print("-------TABUADA DE MULTIPLICAÇÃO-------")
numero = int(input("Digite um número:"))#Recebe a entrada do número a sser multiplicado
print(f"\nTabuada de {numero}:")
for i in range(1, 11):#loop for
    soma = numero * i
    print(f"{i} X {numero} = {soma}")