import os
os.system('cls')

num1 = float(input("Digite o 1º Valor: "))
num2 = float(input("Digite o 2º Valor: "))
num = num1 - num2
if(num < 0):
    num *= -1
cont = 0

while(num != 0):
    if(num % 2 == 0):
        cont += 1
    num -= 1
print(f"Quantidade de numeros pares: {cont}")
