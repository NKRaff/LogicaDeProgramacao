texto = (str(input())).replace(",", "").split()
saida = []
palavras = ""
for i in texto:
    if (i not in palavras):
        saida.append(tuple([i, texto.count(i)]))
        palavras += i
    elif (i.lower() != i.upper() and texto.count(i)==1):
        saida.append(tuple([i, texto.count(i)]))
print(tuple(saida))