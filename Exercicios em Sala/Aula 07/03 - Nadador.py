import os
os.system('cls')

idade = int(input("Digite a idade do nadador: "))

if(idade >= 18):
    print("Classificação: Adulto")
elif(idade >= 14 and idade <= 17):
    print("Classificação: Juvenil B")
elif(idade >= 11 and idade <= 13):
    print("Classificação: Juvenil A")
elif(idade >= 8 and idade <= 10):
    print("Classificação: Infantil B")
elif(idade >= 5 and idade <= 7):
    print("Classificação: Infantil A")
elif(idade <= 0):
    print("Idade Invalida")
else:
    print("Sem Classificação!")
    
