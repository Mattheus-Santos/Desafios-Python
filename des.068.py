#Esse jogo é uma versão simplificada do jogo par ou ímpar. O usuário escolhe um número e se ele escolher par, o computador escolhe ímpar e vice-versa. O jogo acaba quando o usuário perde.
import random

print("=-=" * 10)
print("VAMOS JOGAR PAR OU ÍMPAR?")
print("=-=" * 10)

while True:
    numero_aleatorio = random.randint(1, 10)
    valor = int(input("Digite um valor: "))
    escolha = str(input("Par ou Ímpar? [P/I]: ")).upper().strip()[0]
    teste = numero_aleatorio + valor

    print(f"Você escolheu {valor} e o computador {numero_aleatorio}. Total deu {teste}, que é {'PAR' if teste % 2 == 0 else 'IMPAR'}!")

    if (teste % 2 == 0 and escolha == 'P') or (teste % 2 != 0 and escolha == 'I'):
        print("VOCÊ VENCEU!")
    else:
        print("VOCÊ PERDEU!")
        break

print("O jogo acabou!!!")
