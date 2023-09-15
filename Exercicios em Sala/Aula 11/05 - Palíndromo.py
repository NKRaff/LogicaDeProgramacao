palavra = str(input("Digite uma palavra: ")).replace(" ", "").lower()
palindromo = "" #palavra[::-1 ]
if(palavra.isalpha()):
    for i in range(len(palavra)):
        palindromo += palavra[-i-1]
    
    if(palavra == palindromo):
        print("É um palíndromo!")
    else:
        print("Não é um palíndromo!")
else:
    print("Palavra Invalida!")
