a = int(input("Digite a primeira reta:"))
b = int(input("Digite a segunda reta:"))
c = int(input("Digite a terceira reta:"))

if a + b > c and b + c > a and a + c > b:
    print(f"{a}, {b} e {c}, podem formar um triângulo.")
else:
    print(f"{a}, {b}, e {c}, não podem formar um triâgulo.")