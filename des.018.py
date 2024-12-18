from math import radians, sin, cos, tan
ang = int(input("Digite o número do ângulo: "))
rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)

print("O ângulo no valor de {} possui seno {:.2f}, cosseno {:.2f} e tangente {:.2f}!".format(ang, seno, cosseno, tangente))