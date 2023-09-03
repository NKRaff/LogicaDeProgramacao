# Faça um Programa que peça o raio de um círculo,
# calcule e mostre sua área.

import os
import math
os.system('cls')

raio = float(input("Digite o raio: "))
area = math.pi * raio**2

print(f"A área é: {area:.2f}")
