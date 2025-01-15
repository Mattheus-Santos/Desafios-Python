#Esse programa lê o nome, idade e sexo de 4 pessoas e determina a média de idade do grupo, o nome do homem mais velho e quantas mulheres são menores de 20 anos.
soma_idade = 0
contador_de_mulheres_jovens = 0
homem_maisvelho_nome = 0
homem_maisvelho_idade = 0



for i in range(1, 5):
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Sexo [M/F]: "))

    soma_idade += idade
    if sexo == 'M'and idade > homem_maisvelho_idade:
        homem_maisvelho_nome = nome
        homem_maisvelho_idade = idade
    elif sexo == 'F' and idade < 20:
        contador_de_mulheres_jovens += 1

    print(f"------{i}ª pessoa.------")
    print(f"Nome:{nome}")
    print(f"Idade:{idade}")
    print(f"Sexo:{sexo}")

media_idade = soma_idade / 4
print(f"A média de idade é: {media_idade}")
print(f"O homem mais velhor é: {homem_maisvelho_nome}")
print(f"{contador_de_mulheres_jovens} mulheres são menores de 20 anos!")