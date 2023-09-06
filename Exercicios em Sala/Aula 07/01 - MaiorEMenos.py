import os
os.system('cls')

num1 = int(input("Digite o 1º Numero: "))
num2 = int(input("Digite o 2º Numero: "))
num3 = int(input("Digite o 2º Numero: "))

if(num1 >= num2 and num1 >= num3):
    print("Maior: {}".format(num1))
    if(num2 >= num3):
        print("Menor: {}".format(num3))
    else:
        print("Menor: {}".format(num2))

elif(num2 >= num1 and num2 >= num3):
    print("Maior: {}".format(num2))
    if(num1 >= num3):
        print("Menor: {}".format(num3))
    else:
        print("Menor: {}".format(num1))

else:
    print("Maior: {}".format(num3))
    if(num1 >= num2):
        print("Menor: {}".format(num2))
    else:
        print("Menor: {}".format(num1))

    
