import datetime
ano_nascimento = int(input("Qual o ano de nascimento?:"))
ano_atual = datetime.datetime.now().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print("Mirim.")
elif idade > 9 and idade <= 14:
    print("Infantil.")
elif idade > 14 and idade <= 19:
    print("Junior")
elif idade == 20:
    print("Sênior")
elif idade > 20:
    print("Master")