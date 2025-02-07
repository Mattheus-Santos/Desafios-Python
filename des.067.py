#Esse programa lê um número inteiro e mostra a tabuada desse número. O programa para quando o usuário digitar um número negativo.
print("==" * 20)
print("TABUADA")
print("==" * 20)
cont = 1
while True:
    num = int(input("Digite o número que quer na tabuada: "))
    if num < 0:
        break
    cont = 1
    while cont <= 10:
        res = num * cont
        print(f"{num} X {cont} = {res}")
        cont += 1
    print("==" * 20)

print(f"A tabuada acabou!!!")