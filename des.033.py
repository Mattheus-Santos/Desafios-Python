a = int(input("Digite um número:"))
b = int(input("Digite um número:"))
c = int(input("Digite um número:"))

if a > b and a > c:
    print(f"{a} é o número maior.")
elif b > a and b > c:
    print(f"{b} é o número máior.")
else:
    print(f"{c} é o número maior.")

if a < b and a < c:
    print(f"{a} é o número menor.")
elif b < a and b < c:
    print(f"{b} é o número menor.")
else:
    print(f"{c} é o número menor.")