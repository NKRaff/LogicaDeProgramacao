# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

import os
os.system('cls')

fahrenheit = float(input("Digite a temperatura em °F: "))

celsius = int(5 * ((fahrenheit - 32) / 9))
print(f"{celsius} °C")
