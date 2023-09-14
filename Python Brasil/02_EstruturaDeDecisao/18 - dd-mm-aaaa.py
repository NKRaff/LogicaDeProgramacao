# Faça um Programa que peça uma data no formato 
# dd/mm/aaaa e determine se a mesma é uma 
# data válida.

dia = int(input("Dia: "))

if (dia > 0 and dia < 32):
    mes = int(input("Mês: "))
    if (mes > 0 and mes < 13):
        ano = int(input("Ano: "))
        print(f"{dia} / {mes} / {ano}")
    else: print("Mês Invalido!")
else: print("Dia Invalido!")

