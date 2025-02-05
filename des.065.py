#Esse programa lê vários números inteiros e calcula a média, o maior e o menor número digitado. O programa pergunta se o usuário quer continuar digitando números.
lista = []
while True:
    try:
        num = int(input("Digite um número: "))
        lista.append(num)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    novo = input("Quer continuar? [S/N]: ").strip().upper()
    if novo == 'N':
        break

if lista:
    media = sum(lista) / len(lista)
    maior = max(lista)
    menor = min(lista)
    print(f"A média dos números é {media}, o maior número é {maior} e o menor é {menor}!")
else:
    print("Nenhum número foi inserido.")
