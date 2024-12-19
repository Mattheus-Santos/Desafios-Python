note1 = int(input("Digite e primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))

media = int((nota2 + note1) / 2)

if media >= 7:
    print("APROVADO.")
elif media == 5 or media == 6:
    print("RECUPERAÇÃO.")
elif media < 5:
    print("REPROVADO.")
