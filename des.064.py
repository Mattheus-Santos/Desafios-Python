#Esse programa imprime números digitados pelo usuário e depois informa quantos números foram digitados.

print(f"Digite um número a seguir, para sair digite 999.")
contador = 0
lista = []
num = 0
while num != 999:
    num = int(input(f"Digite um número: "))
    lista.append(num)
    contador += 1


print(f"Foram digitados {len(lista) - 1} números.")