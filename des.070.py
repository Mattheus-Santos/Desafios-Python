#Esse programa lê o nome e o preço de vários produtos e mostra o total da compra, quantos produtos custam mais de 10.00 R$ e o nome do produto mais barato.
print("=-=" * 10)
print(f"LOJA SUPER BARATÃO")
print("=-=" * 10)
prod = 0
cont = 0
total = 0
menor = 0
barato = " "

while True:
    nome_produto = input(f"Nome do produto: ")
    preco = float(input(f"Preço do produto: "))
    cont += 1
    total += preco
    if preco > 10:
        prod += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome_produto

    continuar = input(f"Quer continuar?[S/N]: ").upper().strip()[0]
    if continuar == 'N':
        break

print("=-=" * 10)
print(f"FIM DO PROGRAMA")
print("=-=" * 10)
print(f"O total da compra foi {total :.2f}R$.")
print(f"{prod} produtos custaram acima de 10.00 R$")
print(f"O produto mais barato foi {barato} que custa {menor :.2f}R$.")