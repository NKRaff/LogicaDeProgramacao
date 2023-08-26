import os
os.system('cls')

palavra = str(input("Digite a palavra: ").strip().lower().split())[2:-2]
palavra = palavra.replace("'", "")
palavra = palavra.replace(",", "")

palavraSecreta = []

for x in palavra:
    if (x == " "):
        palavraSecreta.append("-")
    else: 
        palavraSecreta.append("_")

dica = str(input("Digite uma dica: "))
numTentativa = int(input("Digite o numero de tentativas: "))
os.system('cls')

contadorLinhas = len(palavra)
gameContinue = True 

while(gameContinue == True):
    os.system('cls')
    cont = 0
    print(f"Dica: {dica}")
    print(f"Tentativas: {numTentativa}\n")
    for x in palavraSecreta:
        print(f"{x} ", end="")
    letra = str(input("\nDigite uma Letra: "))

    perdeuTentativa = True
    for x in palavra:
        if (letra == x):
            palavraSecreta[cont] = palavraSecreta[cont].replace("_", letra)
            perdeuTentativa = False
        cont += 1
    if (perdeuTentativa == True):
        numTentativa -= 1
    
    contLinha = 0
    for x in palavraSecreta:
        if (x == "_"):
            contLinha += 1
    if (contLinha == 0):
        os.system('cls')

        print("Acertou!")
        print(f"Dica: {dica}")
        print("Palavra: ", end="")
        for x in palavra:
            print(f"{x}", end="")
        gameContinue = False


    if (numTentativa == 0):
        os.system('cls')

        print("Perdeu! As tentativas acabaram")
        print(f"Dica: {dica}")
        print("Palavra: ", end="")
        for x in palavra:
            print(f"{x}", end="")
        gameContinue = False
        
