# Faça um programa que pergunte o preço de três produtos e informe qual 
# produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o 1º produto: "))
produto2 = float(input("Digite o 2º produto: "))
produto3 = float(input("Digite o 3º produto: "))

menor = produto1
produto = "Primeiro"

if (produto2 < menor): menor = produto2; produto = "Segundo"
if (produto3 < menor): menor = produto3; produto = "Terceiro"

print(f"O {produto} produto é o mais barato")