from datetime import datetime

data = input("Digite uma data no formato dd/mm/aaaa: ")
data = datetime.strptime(data, "%d/%m/%Y")

dia_semana = data.weekday()
print(dia_semana)
# 0 = Segunda-feira
# 1 = Terça-feira
# 2 = Quarta-feira
# 3 = Quinta-feira
# 4 = Sexta-feira
# 5 = Sábado
# 6 = Domingo

if dia_semana == 0:
    print("Segunda-feira")
elif dia_semana == 1:
    print("Terça-feira")
elif dia_semana == 2:
    print("Quarta-feira")
elif dia_semana == 3:
    print("quinta-feira")
elif dia_semana == 4:
    print("sexta-feira")
elif dia_semana == 5:
    print("Sabado")
elif dia_semana == 6:
    print("Domingo")
else:
    print("erro")