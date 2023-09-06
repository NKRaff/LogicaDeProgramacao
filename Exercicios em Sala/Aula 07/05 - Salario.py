import os
os.system('cls')

salario = float(input("Digite o Salario: "))
codigo = float(input("Digite o Codigo: "))
novoSalario = 0

if(codigo == 310):
    novoSalario = salario * 1.05
elif(codigo == 465):
    novoSalario = salario * 1.075
elif(codigo == 885):
    novoSalario = salario * 1.1
else:
    novoSalario = salario * 1.15

print(f"Salario antigo: {salario}")
print(f"Novo salario: {novoSalario}")
print(f"Diferença de salario: {novoSalario - salario}")
