# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
#   a) Para homens: (72.7*h) - 58
#   b) Para mulheres: (62.1*h) - 44.7

import os
os.system('cls')

altura = float(input("Digite a altura(m): "))
homem = (72.7 * altura) - 58
mulheres = (62.1 * altura) - 44.7

print(f"Peso Ideal(Homem): {homem:.2f}Kg")
print(f"Peso Ideal(Homem): {mulheres:.2f}Kg")