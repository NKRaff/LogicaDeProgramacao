import os
os.system('cls')

num = int(input("Digite um numero: "))
fatorial = 1

while(num != 0):
    fatorial *= num
    num -= 1

print(f"O Fatorial é: {fatorial}")

