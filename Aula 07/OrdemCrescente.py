import os
os.system('cls')

num1 = float(input("Digite o 1º Valor: "))
num2 = float(input("Digite o 2º Valor: "))
num3 = float(input("Digite o 3º Valor: "))

if(num1 >= num2 and num1 >= num3):
    if(num2 >= num3):
        print("{}, {}, {}".format(num1, num2, num3))
    else:
        print("{}, {}, {}".format(num1, num3, num1))

elif(num2 >= num1 and num2 >= num3):
    if(num1 >= num3):
        print("{}, {}, {}".format(num2, num1, num3))
    else:
        print("{}, {}, {}".format(num2, num3, num1))

else:
    if(num2 >= num1):
        print("{}, {}, {}".format(num3, num2, num1))
    else:
        print("{}, {}, {}".format(num3, num1, num2))
        
