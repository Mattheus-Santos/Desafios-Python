#Esse programa lê vários números inteiros e calcula a soma deles. O programa para quando o usuário digitar 999.
n = s = 0
cont = 0
while True:
    n = int(input(f"Digite um número: "))
    if n == 999:
        break
    s += n
    cont += 1
print(f"Você digitou {cont} númeors e {s} é a soma de todos os números.")