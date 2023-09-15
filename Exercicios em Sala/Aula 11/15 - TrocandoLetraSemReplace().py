palavra = str(input("Digite uma palavra: "))
l1 = str(input("Digite a 1ª Letra: "))
l2 = str(input("Digite a 2ª Letra: "))
novaPalavra = ""

for i in palavra:
    if (i == l1): novaPalavra += l2
    elif (i == l2): novaPalavra += l1
    else: novaPalavra += i

print(f"Nova Palavra: {novaPalavra}")
