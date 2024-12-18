import random
aluno1 = input("Digite o nome do aluno:")
aluno2 = input("Digite o nome do aluno:")
aluno3 = input("Digite o nome do aluno:")
aluno4 = input("Digite o nome do aluno:")

nomes = [aluno1, aluno2, aluno3, aluno4]
nome_sorteado = random.choice(nomes)

print("Os alunos sorteados foram {}, {}, {} e {} e o escolhido foi: {}".format(aluno1, aluno2, aluno3, aluno4, nome_sorteado))