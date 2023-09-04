# Faça um Programa que peça dois números e 
# imprima o maior deles.

num1 = float(input("Digite o 1º numero: "))
num2 = float(input("Digite o 2º numero: "))

if (num1 > num2): print(f"Maior numero: {num1}")
elif (num1 < num2): print(f"Maior numero: {num2}")
else: print("1º e 2º numero são iguais!")

