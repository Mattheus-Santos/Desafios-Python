#Ess programa que lê o primeiro termo e a razão de uma PA. Mostrando os 10 primeiros termos dessa progressão.
termo = int(input("Primeiro termo:"))
razao = int(input("Razão:"))

decimo = termo + (15 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print(i, end="-->")
print("ACABOU.")
