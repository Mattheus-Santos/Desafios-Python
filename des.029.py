velocidade_veiculo = int(input("Qual a velocidade do veículo?:"))

if velocidade_veiculo > 80:
    multa = (velocidade_veiculo - 80) * 7
    print(f"ATENÇÃO! sua velocidade é: {velocidade_veiculo}Km/h, Você ultrapassou o limite permitido: Multado!")
    print(f"Valor da multa: {multa:.2f}R$.")
else:
    print(f"Veículo a {velocidade_veiculo}Km/h, dentro da velocidade permitida.")