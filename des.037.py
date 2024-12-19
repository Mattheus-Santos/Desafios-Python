numero = int(input("Digite um número:"))
escolha = int(input("Escolha 1 para converter em binário, 2 para octal e 3 para hexadecimal:"))

if escolha == 1:
    binario = bin(numero)
    print(binario)
elif escolha == 2:
    binario = oct(numero)
    print(binario)
elif escolha == 3:
    binario = hex(numero)
    print(binario)