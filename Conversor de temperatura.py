conversao = int(input("qual conversao voce deseja fazer? \n (1) celsius para fahrenheit: \n (2) celsius para kelvin: \n (3) fahrenheit para celsius: \n (4) fahrenheit para kelvin: \n (5) kelvin para celsius: \n (6) kelvin para fahrenheit:\n"))
# pede a informação para o usuario escolher qual conversão ele deseja fazer, celsius para fahrenheit ou fahrenheit para celsius


if conversao == 1:
    celsius = float(input("Digite a temperatura em Celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}°F")
elif conversao == 2:
    celsius = float(input("Digite a temperatura em Celsius:"))
    kelvin = celsius + 273.15
    print(f"A temperatura em Kelvin é: {kelvin:.2f}K")
elif conversao == 3:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit:"))
    celsius = (fahrenheit - 32) * 5/9
    print(f"A temperatura em Celsius é: {celsius:.2f}ºC")
elif conversao == 4:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit:"))
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    print(f"A temperatura em Kelvin é: {kelvin:.2f}K")
elif conversao == 5:
    kelvin = float(input("Digite a temperatura em Kelvin:"))
    celsius = kelvin - 273.15
    print(f"A temperatura em Celsius é: {celsius:.2f}ºC")
elif conversao == 6:
    kelvin = float(input("Digite a temperatura em Kelvin:"))
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}ºF")
else:
    print("Opção inválida. Tente novamente.")