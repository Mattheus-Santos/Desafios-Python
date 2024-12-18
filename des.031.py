viagem = int(input("Digite quantos quilômetros é a sua viagem:"))

if viagem <= 200:
    preco_passagem = viagem * 0.50
    print(f"O valor da sua passagem é: {preco_passagem:.2f}R$.")
elif viagem > 200:
    preco_passagem = viagem * 0.45
    print(f"O valor da passagem é: {preco_passagem:.2f}R$")