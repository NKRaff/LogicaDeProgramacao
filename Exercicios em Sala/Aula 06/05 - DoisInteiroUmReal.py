import os
os.system('cls')

num1 = int(input("Digite um inteiro: "))
num2 = int(input("Digite outro inteiro: "))
num3 = float(input("Digite um real: "))

print(f"O produto do dobro do primeiro com metade do segundo: {(num1**2) * (num2/2)}")
print(f"A soma do triplo do primeiro com o terceiro: {(num1*3 + num3):.2f}")
print(f"O terceiro elevado ao cubo: {num3**3:.2f}")
