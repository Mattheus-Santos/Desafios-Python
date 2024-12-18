
dias_aluguel = int(input("Quantos dias de aluguel?"))
km_rodados = int(input("Quantos KM rodados?"))
diaria_aluguel = 60
km_aluguel = 0.15
valor1 = diaria_aluguel * dias_aluguel
valor2 = km_aluguel * km_rodados
total_pagar = valor1 + valor2
print("Você alugou o carro por {:.2f} dias, e rodou {:.2f} KM, o valor do aluguel ficou:{:.2f}R$!".format(dias_aluguel, km_rodados, total_pagar))

