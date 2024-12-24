# Solicitar o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Solicitar a condição de pagamento
print("Condições de pagamento:")
print("1 - À vista dinheiro/cheque: 10% de desconto")
print("2 - À vista no cartão: 5% de desconto")
print("3 - Em até 2x no cartão: preço formal")
print("4 - 3x ou mais no cartão: 20% de juros")

condicao = int(input("Escolha a condição de pagamento (1-4): "))

# Calcular o valor final com base na condição de pagamento
if condicao == 1:
    valor_final = preco * 0.90
    descricao = "10% de desconto (à vista dinheiro/cheque)"
elif condicao == 2:
    valor_final = preco * 0.95
    descricao = "5% de desconto (à vista no cartão)"
elif condicao == 3:
    valor_final = preco
    descricao = "preço formal (em até 2x no cartão)"
elif condicao == 4:
    valor_final = preco * 1.20
    descricao = "20% de juros (3x ou mais no cartão)"
else:
    valor_final = preco
    descricao = "condição de pagamento inválida"

# Exibir o valor final
print(f"Condição escolhida: {descricao}")
print(f"O valor a ser pago é: R$ {valor_final:.2f}")