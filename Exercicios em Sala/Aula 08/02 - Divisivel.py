import os
os.system('cls')

num = float(input("Digite um numero: "))

if (num % 3 == 0 and num % 4 == 0):
    print(f"{num} é divisivel por 3 e por 4!")
elif (num % 3 == 0):
    print(f"{num} é divisivel por 3!")
elif (num % 4 == 0):
    print(f"{num} é divisivel por 4!")
else:
    print(f"{num} não é divisivel nem por 3 nem por 4!")
