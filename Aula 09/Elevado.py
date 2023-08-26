import os
os.system('cls')

base = float(input("Digite a Base: "))
expoente = float(input("Digite o Expoente: "))
cont = 0

while(cont < expoente):
    base *= base
    cont += 1

print(base)
