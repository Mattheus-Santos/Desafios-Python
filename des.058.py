#Esse programa é um jogo de adivinhação. O computador escolhe um número aleatório entre 0 e 10 e o jogador tem que adivinhar qual foi o número escolhido.s
import random
tent = 0
numero_aleatorio = random.randint(0, 10)
ola = input("Sou seu computador... Vamos brincar? [S/N] ").strip().upper()[0]
if ola == "S":
    # Loop principal
    while True:
        numero = int(input("Escolha um número entre 0 e 10: "))  # Input unificado

        if numero == numero_aleatorio:
            print("Parabéns!! Você acertou!")
            tent += 1
            break  # Sai do loop se acertar
        elif numero < numero_aleatorio:
            print("Meu número é maior!")
            tent += 1
        elif numero > numero_aleatorio:
            print("Meu número é menor!")
            tent += 1

    print(f"Número sorteado: {numero_aleatorio}, {tent} tentativass")
else:
    print(f"Tudo bem, fica para a próxima.")