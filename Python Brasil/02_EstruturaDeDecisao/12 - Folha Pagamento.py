# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os 
# descontos são do Imposto de Renda, que depende do salário bruto 
# (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de 
# horas trabalhadas no mês. (INSS = 10%)
#   Desconto do IR:
#   Salário Bruto até 900 (inclusive) - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.


valorHora = float(input("Digite o valor da hora: R$"))
horasTrabalhadas = float(input("Horas trabalhadas: "))

salarioBruto = valorHora * horasTrabalhadas
sindicato = salarioBruto * 0.03
fgts = salarioBruto * 0.11
inss = salarioBruto * 0.1

if(salarioBruto <= 900): ir = 0; porcentagemIR = 0
elif(salarioBruto <= 1500): ir = salarioBruto * 0.05; porcentagemIR = 5
elif(salarioBruto <= 2500): ir = salarioBruto * 0.1; porcentagemIR = 10
else: ir = salarioBruto * 0.2; porcentagemIR = 20

descontos = sindicato + inss + ir
salarioLiquido = salarioBruto - descontos

print(f"""
Salário Bruto: R${salarioBruto:.2f}
FGTS(11%): R${fgts:.2f}
(-) IR({porcentagemIR}%): R${ir:.2f}
(-) INSS(10%): R${inss:.2f}
(-) Sindicato(3%): R${sindicato:.2f}
Desconto Total: R${descontos:.2f}
Salário Liquido: R${salarioLiquido:.2f}
""")
