#Esse programa lê o nome, idade e sexo de 4 pessoas e determina a média de idade do grupo, o nome do homem mais velho e quantas mulheres são menores de 20 anos.
soma_idade = 0
contador_de_mulheres_jovens = 0
homem_maisvelho_nome = 0
homem_maisvelho_idade = 0



for i in range(1, 5):
    print(f"------{i}ª pessoa.------")
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    soma_idade += idade
    if sexo in 'M'and idade > homem_maisvelho_idade:
        homem_maisvelho_nome = nome
        homem_maisvelho_idade = idade
    elif sexo in 'F' and idade < 20:
        contador_de_mulheres_jovens += 1

    
    

media_idade = soma_idade / 4
print(f"A média de idade do grupo é: {media_idade}")
print(f"O homem mais velho é: {homem_maisvelho_nome} e ele possui: {homem_maisvelho_idade} anos.")
print(f"{contador_de_mulheres_jovens} mulheres são menores de 20 anos!")