import os
os.system('cls')

num = int(input("Digite um numero inteiro: "))

centenas = int(num / 100)
dezenas = int((num - centenas*100) / 10)
unidades = int((num - centenas*100) - dezenas * 10)


if(centenas > 1 and centenas < 100):
    print(f"{centenas} centenas ")
elif (centenas == 1):
    print(f"{centenas} centena ")

if (dezenas > 1 and dezenas < 10):
    print(f"{dezenas} dezenas ")
elif (dezenas == 1):
    print(f"{dezenas} dezena ")

if (unidades > 1 and unidades < 10):
    print(f"{unidades} unidades ")
elif (unidades == 1):
    print(f"{unidades} unidade ")
