import os
os.system('cls')

num1 = int(input("Digite o 1º numero: "))
num2 = int(input("Digite o 2º numero: "))

for i in range(num1, num2):
    if(i % 2 == 0):
        print(i)
