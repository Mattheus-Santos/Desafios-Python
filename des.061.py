#Esse programa é uma progressão aritmética. O usuário digita o primeiro termo e a razão e o programa mostra os 15 primeiros termos da progressão.
termo = int(input(f"Digite o primeiro termo: "))
razao = int(input((f"Digite a razão: ")))

cont = 0
primeiro = termo
while cont != 15:
    print("{}-->".format(primeiro), end=" ")
    primeiro += razao
    cont += 1

    #print(f"{termo}", end="---> ")
print(f"ACABOU!!!", end=" ")