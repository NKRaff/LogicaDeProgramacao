import os
os.system('cls')

peso = float(input("Digite o Peso(Kg): "))
altura = float(input("Digite a Altura(m): "))

imc = peso / altura**2

print(f"Valor do IMC: {imc:.2f}")

if(imc < 20):
    print("Avaliação: Abaixo do normal")
elif(imc >= 20 and imc < 25):
    print("Avaliação: Normal")
elif(imc >= 25 and imc < 30):
    print("Avaliação: Sobrepeso")
elif(imc >= 30 and imc < 35):
    print("Avaliação: Obesidade leve")
elif(imc >= 35 and imc < 40):
    print("Avaliação: Obesidade moderada")
else:
    print("Avaliação: Obesidade mórbida")
