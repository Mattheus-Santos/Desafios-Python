a = int(input("Digite a primeira reta:"))
b = int(input("Digite a segunda reta:"))
c = int(input("Digite a terceira reta:"))

if a + b > c and b + c > a and a + c > b:
    print(f"{a}, {b} e {c}, podem formar um triângulo.")
    if a == b and a == c and b == c:
        print("É um triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("É um triângulo Isósceles.")
    elif a != b and a != c and b != c:
        print("É um triângulo escaleno.")
else:
    print(f"{a}, {b}, e {c}, não podem formar um triâgulo.")