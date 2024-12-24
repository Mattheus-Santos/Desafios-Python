numero = int(input("Digite um número:"))
print("""Escolha uma das bases para conversâo:
[1] Binário 
[2] Octal 
[3] Hexadecimal""")
escolha = int(input("Sua opção:"))

if escolha == 1:
    binario = bin(numero)
    print(binario[2:])
elif escolha == 2:
    binario = oct(numero)
    print(binario[2:])
elif escolha == 3:
    binario = hex(numero)
    print(binario[2:])