import random

# Gerar um número aleatório entre 1 e 100
numero_aleatorio = random.randint(0, 5)

numero = int(input("Adivinhe qual é o número de 0 a 5:"))

if numero == numero_aleatorio:
    print(f"O número aleatório é: {numero_aleatorio}, Parabéns, você acertou!")
elif numero > 5:
    print("ERRO: O número escolhido deve ser entre 0 e 5.")
else:
    print(f"O número aleatótio é:{numero_aleatorio}, Você perdeu!")