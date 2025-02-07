#Esse programa lê o nome, idade e sexo de várias pessoas e determina a média de idade do grupo, o nome do homem mais velho e quantas mulheres são menores de 20 anos.
soma_idade = 0
contador_de_mulheres_jovens = 0
homem_maisvelho_nome = ""
homem_maisvelho_idade = 0
pessoa = 0

while True:
    pessoa += 1
    print(f"------ {pessoa}ª pessoa ------")
    nome = str(input("Digite o nome: "))
    idade = int(input("Digite a idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    soma_idade += idade
    if sexo == 'M' and idade > homem_maisvelho_idade:
        homem_maisvelho_nome = nome
        homem_maisvelho_idade = idade
    elif sexo == 'F' and idade < 20:
        contador_de_mulheres_jovens += 1

    continuar = input("Quer continuar? [S/N]: ").upper().strip()[0]
    if continuar == 'N':
        break

media_idade = soma_idade / pessoa
print(f"\nA média de idade do grupo é: {media_idade:.2f}")
print(f"O homem mais velho é: {homem_maisvelho_nome} e ele possui {homem_maisvelho_idade} anos.")
print(f"{contador_de_mulheres_jovens} mulheres são menores de 20 anos!")
