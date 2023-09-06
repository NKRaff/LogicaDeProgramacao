import os
os.system('cls')

num = int(input("Digite a tabuada: "))
cont = 1

while(cont != 11):
    print(f"{num} x {cont} = {num*cont}")
    cont += 1

