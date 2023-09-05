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