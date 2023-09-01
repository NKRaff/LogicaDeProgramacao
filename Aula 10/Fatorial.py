import os
os.system('cls')

num = int(input("Digite um numero: "))
fatorial = 1

for i in range(num):
    fatorial *= num
    num-=1

print(fatorial)
