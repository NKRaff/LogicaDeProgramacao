import os
os.system('cls')

num = int(input("Digite um numero: "))
soma = 0

print(f"A soma dos  divisores do numero {num} é:")

for i in range(1, num):
    if (num % i == 0 and i != num):
        print(f"{i} + ", end="")
        soma += num / i

print(f"= {soma:.0f}")
