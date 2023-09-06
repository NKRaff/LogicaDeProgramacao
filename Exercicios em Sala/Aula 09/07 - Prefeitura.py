import os
os.system('cls')

mediaSalario = 0
mediaFilhos = 0
maiorSalario = 0
menorSalario = 0
cont = 0

while(True):
    salario = float(input("Digite o Salario: "))
    if(salario < 0):
        break
    filhos = int(input("Digite o Nº de Filhos: "))

    mediaSalario += salario
    mediaFilhos += filhos
    if(salario > maiorSalario):
        maiorSalario = salario
    if(salario < 150):
        menorSalario += 1
    cont += 1

mediaSalario = mediaSalario / cont
mediaFilhos = mediaFilhos / cont
menorSalario = (menorSalario * 100) / cont

print(f"""
Média de salário: R${mediaSalario:.2f}
Média de filhos: {mediaFilhos}
Maior salário: {maiorSalario}
Percentual salário baixo: {menorSalario:.2f}%
""")
