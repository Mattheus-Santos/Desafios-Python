dinheiro = int(input("Quanto você tem, na sua carteira?"))
carteira = dinheiro / 5.79

if carteira >= 1:
    print("Você só pode comprar {:.2f} dólares".format(carteira))
else:
    print("Você não pode comprar dólares")

