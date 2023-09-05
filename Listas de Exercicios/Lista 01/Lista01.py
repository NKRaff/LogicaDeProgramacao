# Aluno: Rafael Felix Rocha

# Questão 1
'''
num = int(input("Digite um numero inteiro: "))
print(f"Numero Digitado: {num}")
'''

# Questão 2
'''
num1 = int(input("Digite o 1º Numero Inteiro: "))
num2 = int(input("Digite o 2º Numero Inteiro: "))
num3 = int(input("Digite o 3º Numero Inteiro: "))
print(f"A soma dos numeros digitados é: {num1 + num2 + num3}")
'''

# Questão 3
'''
num = int(input("Digite um numero inteiro: "))
print(f"Antecessor: {num-1}")
print(f"Sucessor: {num+1}")
'''

# Questão 4
'''
celsius = float(input("Digite a temperatura em °C: "))
fahrenheit = celsius * (9/5) + 32
print(f"°F: {fahrenheit}")
'''

# Questão 5
'''
km = float(input("Digite a velocidade em km/h: "))
m = km/3.6
print(f"Velocidade em m/s: {m}")
'''

# Questão 6
'''
nota1 = float(input("Digite a 1ª Nota"))
nota2 = float(input("Digite a 2ª Nota"))
nota3 = float(input("Digite a 3ª Nota"))
nota4 = float(input("Digite a 4ª Nota"))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Media: {media}")
'''

# Questão 7
'''
real = float(input("Valor: R$"))
cotacao = float(input("Cotação: $"))
dolar = real * cotacao
print(f"Real brasileiro: R${real:.2f}")
print(f"Dólar americano: ${dolar:.2f}")
'''

# Questão 8
'''
raio = float(input("Digite o raio: "))
area = 3.14 * raio**2
print(f"Área do Circulo: {area:.2f}")
'''

# Questão 9
'''
primeiro = 780000 * 0.46
segundo = 780000 * 0.32
terceiro = 780000 - primeiro - segundo

print(f"Primeiro: R${primeiro:.2f}")
print(f"Segundo: R${segundo:.2f}")
print(f"Terceiro: R${terceiro:.2f}")
'''

# Questão 10
'''
num = float(input("Digite um numero: "))
if(num > 0):
    print(f"{num}² = {(num**2):.2f}")
    print(f"√{num} = {(num**0.5):.2f}")
'''

# Questão 11
'''
num = float(input("Digite um numero: "))
if(num % 2 == 0): print(f"O numero {num} é par")
else: print(f"O numero {num} é impar")

if(num > 0): print(f"O numero {num} é positivo")
elif(num < 0): print(f"O numero {num} é negativo")
else: print(f"O numero {num} é neutro")
'''

# Questão 12
'''
nota1 = float(input("Digite a 1ª nota: "))
if (nota1 >= 0 and nota1 <= 10):
    nota2 = float(input("Digite a 2ª nota: "))
    if (nota2 >= 0 and nota2 <= 10):
        print(f"Media: {((nota1 + nota2) / 2):.2f}")
    else: print("Nota Invalida!")
else: print("Nota Invalida!")
'''

# Questão 13
'''
altura = float(input("Altura(Kg): "))
sexo = str(input("Sexo(M/F): ")).upper()
if(sexo == "M"):
    print(f"Peso Ideal: {(72.7 * altura)-58:.2f}kg")
elif(sexo == "F"):
    print(f"Peso Ideal: {(62.1 * altura)-44.7:.2f}kg")
else:
    print("Sexo Invalido!")
'''

# Questão 14
'''
nota1 = float(input("Digite a 1ª nota: "))
if (nota1 >= 0 and nota1 <= 10):
    nota2 = float(input("Digite a 2ª nota: "))

    if (nota2 >= 0 and nota2 <= 10):
        nota3 = float(input("Digite a 2ª nota: "))

        if (nota3 >= 0 and nota3 <= 10):
            media = (nota1*2 + nota2*3 + nota3*5) / 10
            print(f"Media: {media:.2f}")
            
        else: print("Nota Invalida!")
    else: print("Nota Invalida!")
else: print("Nota Invalida!")
'''

# Questão 15
'''
print("Responda apenas com: Sim / Não")
classificacao = 0

pergunta = str(input("Telefonou para a vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Esteve no local do crime? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Mora perto da vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Devia para a vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Já trabalhou com a vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

if (classificacao == 5): print("Assassino")
elif (classificacao == 4 or classificacao == 3): print("Cúmplice")
elif (classificacao == 2): print("Suspeita")
else: print("Inocente")
'''

# Questão 16
'''
idade = int(input("Digite sua idade: "))
tempo = float(input("Tempo de serviço: "))

if(idade >= 65): print("Pode se Aposentar")
elif (tempo >= 30): print("Pode se Aposentar")
elif (idade >= 60 and tempo >= 25): print("Pode se Aposentar")
else: print("Não pode se Aposentar")
'''

# Questão 17
'''
distancia = float(input("Digite a distância(Km): "))
litros = float(input("Digite a quantidade de gasolina consumida(l): "))
kml = distancia / litros
if (kml < 8): print("Venda o carro!")
elif (kml <= 12): print("Econômico!")
else: print("Super econômico!")
'''

# Questão 18
'''
print("Com For: ")
for i in range(1, 101, 1):
    print(i, " ", end="")

print("\nCom While: ")
i = 1
while(i < 101):
    print(i, " ", end="")
    i += 1
'''

# Questão 19
'''
soma = 0
for i in range(10):
    num = float(input(f"Digite o {i+1}º numero: "))
    soma += num
print(f"Soma = {soma}")
'''

# Questão 20
'''
soma = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}º numero inteiro: "))
    soma += num
print(f"Media = {soma/10}")
'''

# Questão 21
'''
soma = 0
cont = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}º numero inteiro: "))
    if(num > 0):
        soma += num
        cont += 1
print(f"Media = {soma/cont}")
'''

# Questão 22
'''
num = int(input("Digite um numero inteiro: "))
i = 0
while(num!=0):
    i += 1
    if(i % 2 != 0): 
        print(i, " ", end="")
        num -= 1
'''

# Questão 23
'''
num = int(input("Digite um numero inteiro: "))
if(num > 0):
    for i in range(num+1):
        print(i, " ", end="")
'''

# Questão 24
'''
num = int(input("Digite um numero inteiro: "))
if(num > 0):
    for i in range(num, 0, -1):
        print(i, " ", end="")
'''

# Questão 25
'''
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
if(num1>num2): x = num1; num1 = num2; num2 = x

soma = 0
multiplicacao = 1
for i in range(num1, num2+1, 1):
    if(i % 2 == 0): soma += i
    else: multiplicacao *= i
print(f"Soma dos pares =  {soma}")
print(f"Multiplicação dos impares = {multiplicacao}")
'''

# Questão 26
'''
for i in range(1, 10, 1):
    print(f"\nTabuada do {i}")
    for j in range(1, 11, 1):
        print(f"{i} x {j} = {i*j}")
'''

# Questão 27
'''
num = int(input("Digite um numero inteiro: "))
cont = 0
if (num > 0):
    for i in range(num):
        for j in range(i+1):
            cont += 1
            print(cont, " ", end="")
        print()
'''
