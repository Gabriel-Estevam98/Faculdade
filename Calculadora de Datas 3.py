import calendar

ano = int(input("Digite o ano que deseja saber se é bissexto"))

verif = calendar.isleap(ano)

if verif == True:
    print(f"O ano que você digitou, {ano}, ele é bissexto.")
else:
    print(f"O ano que você digitou, {ano}, ele não é bissexto.")

