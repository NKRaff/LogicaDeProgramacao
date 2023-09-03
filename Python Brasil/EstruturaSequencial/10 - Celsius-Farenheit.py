# Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.

import os
os.system('cls')

celsius = float(input("Digite a temperatura em °C: "))

fahrenheit = int(celsius * 1.8 + 32)
print(f"{fahrenheit} °F")
