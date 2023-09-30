tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3)
lista = []
for i in tupla:
    if i not in lista:
        lista.append(i)
tupla = sorted(lista)
print(tupla)