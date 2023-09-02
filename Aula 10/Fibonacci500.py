import os
os.system('cls')

ultimo = 1
antiultimo = 0
atual = 0

print("0, 1", end="")
for i in range(2, 500):
    atual = antiultimo + ultimo
    if(atual >= 500): break
    antiultimo = ultimo
    ultimo = atual
    print(f", {atual}", end="")
