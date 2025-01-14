#Esse programa lê o ano de nascimento de 7 pessoas e determina quantas são maiores de idade e quantas são menores de idade.
from datetime import date
atual = date.today().year

soma = 0
cont = 0

for i in range(1, 8):
    ano_nascimento = int(input("Digite seu ano de nascimento:"))
    if atual - ano_nascimento >= 18:
        cont += 1
    else:
        soma += 1
print(f"{cont} pessoas são maiores de idade, e {soma} ainda são menores de idade!")
print(atual)