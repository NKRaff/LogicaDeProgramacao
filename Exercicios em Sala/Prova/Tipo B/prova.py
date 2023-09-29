# Questão 1
'''
texto1 = str(input("Digite o primeiro texto: "))
texto2 = str(input("Digite o segundo texto: "))
novaString1 = ""
novaString2 = ""

for i in texto1:
    if(i not in novaString1): novaString1 += i
for i in texto2:
    if(i not in novaString2): novaString2 += i

for i in texto1:
    if (i in texto2): 
        novaString1 = novaString1.replace(i, "")
        novaString2 = novaString2.replace(i, "")

print(f"1ª String: {novaString1}")
print(f"2ª String: {novaString2}")
'''


# Questão 2
'''
num1 = int(input("Digite o 1º Valor: "))
num2 = int(input("Digite o 2º Valor: "))
multiplicacao = 1
impares = 0

for i in range(num1, num2+1, 1):
    if(i % 2 == 0): multiplicacao *= i
    else: impares+=1

print(f"""
Quantidade de numeros impares: {impares}
Multiplicação dos pares: {multiplicacao}
""")
'''

# Questão 3
'''
listaEmpreencimentos = []
while(True):
    lista = []

    codigo = int(input("Digite o codigo (9999 para sair): "))
    if codigo == 9999: break

    lista.append(codigo)
    lista.append(float(input("Digite a area: ")))
    lista.append(float(input("Digite o valor do empreendimento: R$")))
    lista.append(float(input("Digite o valor do aluguel: R$")))
    lista.append(str(input("Esta alugado? (S/N): ")).upper())

    if lista[4] == "S": status = "Alugado"
    else: status = "Não Alugado"

    listaEmpreencimentos.append(lista)
    print(f"""
Codigo: {lista[0]}
Area: {lista[1]:.2f}m²
Valor do empreendimento: R${lista[2]:.2f}
Valor do aluguel: R${lista[3]:.2f}
Status: {status}
""")
# FIM WHILE 

patrimonioTotal = 0
naoAlugados = 0
arrecadamento = 0
for i in listaEmpreencimentos:
    if i[4] != "S": maior = i[3]; codigoMaior = i[0]
for i in listaEmpreencimentos:
    if i[4] != "S": menor = i[3]; codigoMenor = i[0]

for i in listaEmpreencimentos:
    patrimonioTotal += i[2]
    if i[4] == "S": arrecadamento+=i[3]
    else: 
        naoAlugados+=1
        if(i[3] > maior):
            maior = i[3]
            codigoMaior = i[0]
        if(i[3] < menor):
            menor = i[3]
            codigoMenor = i[0]

print(f"""
Patrimonio Total: R${patrimonioTotal:.2f}
Nº de patrimonios não alugados: {naoAlugados}
Valor mensal arrecadado: R${arrecadamento:.2f}
Empreendimento de:
    Maior Valor: 
        Codigo: {codigoMaior}
        Valor do Aluguel: R${maior:.2f}
    Menor Valor: 
        Codigo: {codigoMenor}
        Valor do Aluguel: R${menor:.2f}
""")
'''

# Questão 4

num = int(input())
print(num)

print(f"{num//100} notas(s) de R$ 100,00")
num -= (num//100)*100
print(f"{num//50} notas(s) de R$ 50,00")
num -= (num//50)*50
print(f"{num//20} notas(s) de R$ 20,00")
num -= (num//20)*20
print(f"{num//10} notas(s) de R$ 10,00")
num -= (num//10)*10
print(f"{num//5} notas(s) de R$ 5,00")
num -= (num//5)*5
print(f"{num//2} notas(s) de R$ 2,00")
num -= (num//2)*2
print(f"{num//1} notas(s) de R$ 1,00")
