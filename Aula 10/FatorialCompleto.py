import os
os.system('cls')

num = int(input("Fatorial de: "))
fatorial = 1

print(f"{num}! = ", end="")

for i in range(num, num>0, -1):
    print(f"{i} x ",end="")
    fatorial *= i
    i-=1

print(f"1 = {fatorial}")
