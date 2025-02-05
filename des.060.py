#Esse programa é um cálculo de fatorial de um número qualquer.

# Inicializar o número cujo fatorial queremos calcular
numero = int(input(f"Digite o número: "))

# Inicializar a variável de resultado
fatorial = 1

# Inicializar um contador
contador = 1
print(f"Calculando fatorial de {numero}!")
# Usar um laço while para calcular o fatorial
while contador <= numero:
    fatorial *= contador
    contador += 1

# Imprimir o resultado
print(f"O fatorial de {numero} é {fatorial}")
