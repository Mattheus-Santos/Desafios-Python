import math
num1 = int(input("Digite o comprimento do cateto oposto: "))
num2 = int(input("Digite o comprimento do cateto adjacente: "))
num3 = math.sqrt(num1 ** 2 + num2 ** 2)
print("O cateto oposto é {:.2f} e o adjacente é {:.2f}, logo, o valor da hipotenusa é:{:.2f}!".format(num1, num2, num3))