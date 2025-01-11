#Esse programa soma todos os números pares que o usuário digitar.
soma = 0  # Inicializa a variável 'soma' com o valor 0. Essa variável será usada para somar os números pares.
cont = 0  # Inicializa a variável 'cont' com o valor 0. Essa variável será usada para contar os números pares.

for i in range(1, 7):  # Inicia um loop que se repete 6 vezes, pois o range(1, 7) inclui os números de 1 a 6.
    num = int(input("Digite um número inteiro:"))  # Solicita ao usuário que digite um número inteiro e converte a entrada para o tipo inteiro.

    if num % 2 == 0:  # Verifica se o número digitado é par. Um número é par se o resto da divisão por 2 for 0.
        soma += num  # Se o número for par, adiciona o valor do número à variável 'soma'.
        cont += 1  # Incrementa o contador de números pares em 1.

print(f"Você informou {cont} números PARES, e a soma foi {soma}!")  # Exibe a quantidade de números pares informados e a soma desses números.