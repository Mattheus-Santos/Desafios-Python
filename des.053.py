frase = str(input("Digite uma frase:")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):# Percorre a string 'junto' de trás para frente e constrói a string 'inverso' caractere por caractere.
    inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}!")
if inverso == junto:
    print("Temos um Palidromo!")
else:
    print("A frase não é um Palidromo!")


print(junto)