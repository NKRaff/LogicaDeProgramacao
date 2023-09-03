# Faça um Programa que calcule a área de um quadrado, 
# em seguida mostre o dobro desta área para o usuário.

import os
os.system('cls')

lado = float(input("Digite o valor do lado: "))
area = lado * lado

print(f"O dobro da área é: {area*2:.2f}")
