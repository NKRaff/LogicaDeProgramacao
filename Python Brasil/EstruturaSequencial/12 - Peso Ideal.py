# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58

import os
os.system('cls')

altura = float(input("Digite a altura(m): "))
peso = (72.7 * altura) - 58

print(f"Peso Ideal: {peso:.2f}Kg")
