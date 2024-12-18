# Solicita ao usuário para digitar um número
numero = int(input("Digite um número:"))

# Exibe a tabuada do número
print(f"\nTabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i  # Corrigido aqui, substituindo "numero * 1" por "numero * i"
    print(f"{numero} x {i} = {resultado}")
