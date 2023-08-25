import os
os.system('cls')

num1 = float(input("Digite o 1º lado: "))
num2 = float(input("Digite o 2º lado: "))
num3 = float(input("Digite o 3º lado: "))

if(num1 + num2 > num3):
    if(num1 == num2 and num2 == num3):
        print("É um Triangulo Equilatero!")
    elif(num1 != num2 and num2 != num3):
        print("É um Triangulo Escaleno!")
    else:
        print("É um Triangulo Isosceles!")
else:
    print("Não é um triangulo!")
