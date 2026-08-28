#Calculadora geométrica
#gabriel estevam (Drops)

import math

forma = input("Informe qual calculo geometrico deseja fazer:\n 1 - área do retângulo:\n 2 - área do triângulo:\n 3 - área do círculo:\n")

if forma == "1":
    base = float(input("Digite o valor da base do retângulo:"))
    altura = float(input("Digite o valor da altura do retângulo:"))
    area = base * altura
    print(f"A área do retângulo é: {area}")
elif forma == "2":
    base = float(input("Digite o valor da base do triângulo:"))
    altura = float(input("Digite o valor da altura do triângulo:"))
    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")
elif forma == "3":
    raio = float(input("Digite o valor do raio do Círculo:"))
    area = math.pi * (raio ** 2)
    print(f"A área do círculo é: {area:.2f}")
else:
    print("Opção inválida. tente novamente.")