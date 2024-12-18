frase = str(input("Digite um frase:")).upper()
print("A letra A aparece {} vezes!".format(frase.count("A")))
print("A letra A aparece a primeira vez na posição {}!".format(frase.find("A")))
print("A letra A aparece pela última vez na posição {}!".format(frase.rfind("A")))