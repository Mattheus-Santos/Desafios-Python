#Esse código determina se um número é primo ou não.
numero = int(input("Digite um número:"))
tot = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(f"{i}", end=" ")

print(f"\n\033[mO número {numero} foi divisível {tot} vezes!")
if tot == 2:
    print(f"E por isso ele é primo!")
else:
    print(f"E por isso ele não é primo!")