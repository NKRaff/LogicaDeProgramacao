# Faça um Programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a 
# tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões 
# de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas 
#   e os respectivos preços em 3 situações:
#       - comprar apenas latas de 18 litros;
#       - comprar apenas galões de 3,6 litros;
#       - misturar latas e galões, de forma que o desperdício de tinta seja menor.
#         Acrescente 10% de folga e sempre arredonde os valores para cima, 
#         isto é, considere latas cheias.

import os
os.system('cls')

metros = float(input("Digite a área a ser pintada(m²): "))
litros = metros / 6

#Calculo apenas Latas
latas = int(litros / 18 + 1)
preco = latas * 80

print(f"""
Você vai precisar de:
{latas}x Latas de Tinta
Preço: R${preco:.2f}
""",end="")

#Calculo apenas Galões
galoes = int(litros / 3.6 + 1)
preco = galoes * 25

print(f"""
Você vai precisar de:
{galoes}x Galões de Tinta
Preço: R${preco:.2f}
""",end="")

#Calculo Latas e Galões
latas = int(litros / 18)
galoes = int((litros % 18)/3.6 + 1)
preco = (latas * 80) + (galoes * 25)

print(f"""
Você vai precisar de:
{latas}x Latas de Tinta
{galoes}x Galões de Tinta
Preço: R${preco:.2f}
""")

