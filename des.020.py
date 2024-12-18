import random
aluno1 = input("Digite o nome do aluno:")
aluno2 = input("Digite o nome do aluno:")
aluno3 = input("Digite o nome do aluno:")
aluno4 = input("Digite o nome do aluno:")

nomes = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(nomes)

print("Os alunos são {}, {}, {} e {} e a ordem de apresetação é: {}".format(aluno1, aluno2, aluno3, aluno4, nomes))