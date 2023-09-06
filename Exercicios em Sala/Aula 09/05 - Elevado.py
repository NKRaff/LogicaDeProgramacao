import os
os.system('cls')

base = float(input("Digite a Base: "))
expoente = float(input("Digite o Expoente: "))
res = 1
cont = 0

while(cont < expoente):
    res *= base
    cont += 1

print(res)
