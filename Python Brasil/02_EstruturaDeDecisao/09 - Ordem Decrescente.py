# Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input("Digite o 1º numero: "))
num2 = float(input("Digite o 2º numero: "))
num3 = float(input("Digite o 3º numero: "))
maior = num1
menor = num1

if (num2 > maior): maior = num2
if (num3 > maior): maior = num3

if (num2 < menor): menor = num2
if (num3 < menor): menor = num3

meio = (num1 + num2 + num3) - maior - menor

print(f"{maior}, {meio}, {menor}")
