import os
os.system('cls')

base = int(input("Digite a base: "))
expoente = int(input("Digite a expoente: "))
res = 1

for i in range(expoente):
    res *= base

print(res)