import os
os.system('cls')

num = int(input("Que termo deseja encontrar: "))
ultimo=1
anteultimo=1

if (num == 1):
    print("1")
elif (num == 2):
    print("1, 1")
elif (num == 0):
    print("0")
else:
    print("1, 1", end="")
    for i in range(2, num):
        novo = ultimo + anteultimo
        anteultimo = ultimo
        ultimo = novo
        print(f", {novo}", end="")
