nome = str(input("Digite seu nome completo:")).strip()
nome1 = nome.split()
print(f"Prazer, {nome}!")
print(f"Seu primeito nome é:{nome1[0]}")
print(f"Seu segundo nome é:{nome1[-1]}")