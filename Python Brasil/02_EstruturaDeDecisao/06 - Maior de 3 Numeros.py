# Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input("Digite o 1º numero: "))
num2 = float(input("Digite o 2º numero: "))
num3 = float(input("Digite o 3º numero: "))
maior = num1

if (num2 > maior): maior = num2
if (num3 > maior): maior = num3

print(f"Maior: {maior}")
