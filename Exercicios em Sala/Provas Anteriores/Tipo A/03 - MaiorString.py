listaDeString = []

while(True):
    texto = str(input("Digite uma string qualquer(0 = Sair): "))
    if (texto == "0"): break
    else: 
        for letra in texto:
            if (texto.count(letra) == 1): Aprovada = True
            else: Aprovada = False
        if(Aprovada == True): listaDeString.append(texto)

maior = len(listaDeString[0])
posicao = 0

for i in range(len(listaDeString)):
    if (len(listaDeString[i]) > maior):
        maior = len(listaDeString[i])
        posicao = i

print(f"Maior String: {listaDeString[posicao]}")
