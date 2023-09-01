# COPIADO

import os
os.system('cls')

num = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (num==1):
    print("0, 1")
elif (num == 2):
    print("0, 1, 2")
else:
    print("0, 1", end="")
    for i in range(2,num,2):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        print(f", {termo}",end="")
        
