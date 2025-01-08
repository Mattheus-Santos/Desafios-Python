#Esse é um programa que soma todos os números divisíveis por 3 entre 1 e 500.

# Inicializa a soma
soma_total = 0

# Percorre os números de 1 a 499
for i in range(1, 500):
    if i % 3 == 0  and i % 2 != 0:
        #print(i, end=" ")
        soma_total += i  # Adiciona o número à soma total

# Exibe a soma total
print("\nA soma de todos os números divisíveis por 3 é:", soma_total)
