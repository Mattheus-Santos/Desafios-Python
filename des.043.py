peso = float(input("Qual seu peso?:"))
altura = float(input("Qual sua altura?:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 25:
    print("Peso ideal.")
elif imc > 25 and imc <= 29:
    print("Sobrepeso.")
elif imc >= 30 and imc <= 34:
    print("Obesidade grau I.")
elif imc >= 35 and imc <= 39:
    print("Obesidade grau II.")
elif imc >= 40:
    print("Obesidade grau III.")