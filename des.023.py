numero = input("Digite um número de 0 a 9999:")

str_numero = str(numero)
str_numero = str_numero.zfill(4)
print(f"Milhar:{str_numero[-4]}")
print(f"Centena:{str_numero[-3]}")
print(f"Dezena:{str_numero[-2]}")
print(f"Unidade:{str_numero[-1]}")