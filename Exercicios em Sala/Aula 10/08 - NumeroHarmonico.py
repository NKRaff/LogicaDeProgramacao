import os
os.system('cls')

num = int(input("Digite um numero: "))
harmonico = 1

print("1", end="")
for i in range(2, num+1):
    harmonico += 1/i
    print(f" + 1/{i}", end="")

print(f"\nNumero Harmonico: {harmonico:.2f}")

