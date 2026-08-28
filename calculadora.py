calculo1 = float(input("Digite o primeiro numero: "))
simbolo = input("insira qual tipo de Simbolos de calculo vc deseja Adicao (+) Subtracao (-) Multiplicacao (*) Divisao (/)" )
calculo2 = float(input("Digite o segundo numero: "))

if simbolo == "+": 
    total = calculo1 + calculo2 
    print (f"o resultado é {total}")
elif simbolo == "-":
    total = calculo1 - calculo2
    print (f"o resultado é {total}")
elif simbolo == "*":
    total = calculo1 * calculo2
    print (f"o resultado é {total}")
elif simbolo == "/":
    if calculo2 == 0:
        print("Símbolo inválido. Tente novamente.")
    else:
        total = calculo1 / calculo2
        print (f"o resultado é {total}")
else:
    print("Simbolo invalido, tente novamente")