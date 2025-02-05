#Esse programa é uma progressão aritmética. O usurário pode escolher quantos termos ele quer ver a mais.
primeiro = int(input(f"Digite o primeiro termo: "))
razao = int(input((f"Digite a razão: ")))

cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{}-->".format(primeiro), end=" ")
        primeiro += razao
        cont += 1
    print("PAUSA")
    mais = int(input(f"Quantas P.A você quer a mais?: "))

print(f"Progressão finalizada com {total} de termos mostrados!!!")