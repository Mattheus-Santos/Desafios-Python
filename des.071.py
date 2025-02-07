#Esse programa simula um caixa eletrônico. O usuário digita o valor que deseja sacar e o programa informa quantas cédulas de cada valor serão entregues. O programa para quando o usuário digitar 0.

print("=" *20)
print('{:^20}'.format('BANCO STR'))
print("=" *20)

valor = int(input("Qual valor você quer sacar? R$:"))
total = valor
ced = 50
total_ced = 0

while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"Total de {total_ced} cédulas de R$ {ced}.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

print("=" *20)
print('{:^20}'.format('OBRIGADO POR USAR NOSSOS SERVIÇOS'))
print("=" *20)
