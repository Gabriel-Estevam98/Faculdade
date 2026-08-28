txt = input("Digite um texto:")
dado = input("Digite qual tipo de manipulação de texto você deseja fazer: \n (maiusculo) para converter o texto em maiúsculas \n (minusculo) para converter o texto em minúsculas \n (capitalizar) para capitalizar a primeira letra do texto \n (contar) para contar o número de palavras no texto \n (inverter) para inverter a ordem das letras no texto \n (encontrar) para encontrar quantas vezes uma palavra aparece no texto: \n")


if dado == "maiusculo":
    print(txt.upper())
    #upper() é um método que converte todos os caracteres de uma string para maiúsculas.
elif dado == "minusculo":
    print(txt.lower())
    #lower() é um método que converte todos os caracteres de uma string para minúsculas.
elif dado == "capitalizar":
    print(txt.capitalize())
    #capitalize() é um método que converte o primeiro caractere de uma string para maiúscula e os demais para minúscula.
elif dado == "contar":
    palavra = txt.split()
    contar = len(palavra)
    print(f"o número de palavras no texto é: {contar}")
    #split() é um método que divide uma string em uma lista de palavras, usando espaços em branco como delimitadores. len() é uma função que retorna o número de elementos em uma lista.
elif dado == "inverter":
    print(txt[::-1])
    #[::-1] é uma técnica de fatiamento de strings que inverte a ordem dos caracteres em uma string.
elif dado == "encontrar":
    palavra = input("Digite a palavra que deseja encontrar no texto:")
    contar = txt.count(palavra)
    print(f"A palavra '{palavra}' aparece {contar} vezes no texto.")
else:
    print("opção inválida, tente novamente")

