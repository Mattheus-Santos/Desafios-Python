import datetime
ano_Nascimento = int(input("Digite seu ano de nascimento:"))
# Obter o ano atual
ano_atual = datetime.datetime.now().year

if ano_atual - ano_Nascimento == 17 or ano_atual - ano_Nascimento == 18:
    print("HORA DE SE ALISTAR!")
elif ano_atual - ano_Nascimento <= 16:
    print("VOCÊ AINDA VAI SE ALISTAR.")
else:
    print("JÁ PASSOU DO PRAZO DE VOCÊ SE ALISTAR.")