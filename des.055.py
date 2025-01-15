#Esse programa lê o peso de 5 pessoas e determina qual é o maior e o menor peso.
lista = []
for i in range(1, 6):
    peso = int(input("Qual o seu peso?:"))
    lista.append(peso)
#print(lista)
maior = max(lista)
menor = min(lista)
print(f"o maior peso é:{maior:.2f} KG e o menor:{menor:.2f} KG!")