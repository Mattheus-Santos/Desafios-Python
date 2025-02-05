#Esse programa é uma sequência de Fibonacci. O usuário digita quantos termos ele quer ver da sequência.
termos_desejados = int(input(f"Quantos termos você quer para a sequência?: "))

num1 = 0
num2 = 1
sequencia = []
contador = 0

while contador <= termos_desejados:
    #print(num1)
    sequencia.append(num1)
    proximo = num1 + num2
    num1 = num2
    num2 = proximo
    contador += 1
print(sequencia)
