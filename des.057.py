#Esse programa lê o nome, idade e sexo de 4 pessoas e determina a média de idade do grupo, o nome do homem mais velho e quantas mulheres são menores de 20 anos.
sexo = str(input("Digite seu sexo (M/F): ")).strip().upper()[0]

while sexo not in ['M', 'F']:
    sexo = str(input('Dados inválidos. Por favor, digite seu sexo (M/F): ')).strip().upper()[0]

if sexo == 'M':
    print("Seu sexo é masculino!")
elif sexo == 'F':
    print("Seu sexo é feminino!")