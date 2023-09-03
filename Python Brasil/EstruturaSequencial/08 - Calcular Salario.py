# Faça um Programa que pergunte quanto você ganha por hora 
# e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

import os
os.system('cls')

dinheiro = float(input("Digite o sálario/h: "))
horas = float(input("Digite as horas trabalhadas: "))

print(f"O sálario nesse mês é: R${(dinheiro * horas):.2f}")