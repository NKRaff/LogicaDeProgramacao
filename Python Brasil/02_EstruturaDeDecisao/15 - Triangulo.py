# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá 
# informar se os valores podem ser um triângulo. Indique, caso os lados 
# formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#   Três lados formam um triângulo quando a soma de quaisquer dois lados 
#   for maior que o terceiro;
#   Triângulo Equilátero: três lados iguais;
#   Triângulo Isósceles: quaisquer dois lados iguais;
#   riângulo Escaleno: três lados diferentes;


num1 = float(input("Digite o 1º lado: "))
num2 = float(input("Digite o 2º lado: "))
num3 = float(input("Digite o 3º lado: "))

if(num1 + num2 > num3 and
   num1 + num3 > num3 and
   num2 + num3 > num1):
    if(num1 == num2 and num1 == num3 and num2 == num3):
        print("É um Triângulo Equilátero!")
    elif(num1 != num2 and num1 != num3 and  num2 != num3):
        print("É um Triângulo Escaleno")
    else:
        print("É um Triângulo Isósceles")
else:
    print("Não é um Triângulo")
