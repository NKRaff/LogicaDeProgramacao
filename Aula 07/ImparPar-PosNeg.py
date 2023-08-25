import os
os.system('cls')

num = int(input("Digite um numero: "))

if(num % 2 == 1):
    print("Impar")
elif(num % 2 == 0):
    print("Par")

if(num > 0):
    print("Positivo")
elif(num < 0):
    print("Negativo")
else:
    print("Numero Neutro")