num = int(input("Digite o numero de camadas do triangulo: "))
cont = 0
for i in range(num):
    for j in range(i+1):
        cont += 1
        print(cont, " ", end="")
    print()