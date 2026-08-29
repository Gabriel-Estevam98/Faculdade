from datetime import datetime

data1 = input("digite a primeira data:")
data2 = input("digite a segunda data:")

data1 = datetime.strptime(data1, "%d/%m/%Y")
data2 = datetime.strptime(data2, "%d/%m/%Y")

resultado = data2 - data1

print(resultado.days)