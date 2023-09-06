import os
os.system('cls')

horasValor = float(input("Digite o valor da hora: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salarioBruto = horasTrabalhadas * horasValor
sindicato = salarioBruto * 0.03
fgts = salarioBruto * 0.11
inss = salarioBruto * 0.1
ir = 0


if(salarioBruto <= 900):
    ir = 0
elif(salarioBruto > 900 and salarioBruto <= 1500):
    ir = salarioBruto * 0.05
elif(salarioBruto > 1500 and salarioBruto <= 2500):
    ir = salarioBruto * 0.1
else:
    ir = salarioBruto * 0.2

print(f"""
Salário bruto:      R$ {salarioBruto:.2f}
(-) IR:             R$ {ir:.2f}
(-) INSS(10%):      R$ {inss:.2f}
(-) Sindicato(3%):  R$ {sindicato:.2f}
FGTS(11%):          R$ {fgts:.2f}
Total de desconto:  R$ {(ir + inss + sindicato):.2f}
Salario Liquido:    R$ {(salarioBruto - (ir + inss + sindicato)):.2f}
""")

