# Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre:
#   a) o produto do dobro do primeiro com metade do segundo .
#   b) a soma do triplo do primeiro com o terceiro.
#   c) o terceiro elevado ao cubo.

import os
os.system('cls')

primeiro = int(input("Digite o 1º inteiro: "))
segundo = int(input("Digite o 2º inteiro: "))
terceiro = int(input("Digite o um real: "))

print(f"""
a) {((primeiro*2) * (segundo/2)):.2f}
b) {(primeiro*3) + terceiro:.2f}
c) {terceiro**3:.2f}
""")
