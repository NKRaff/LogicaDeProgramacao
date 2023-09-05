num = int(input("Digite um numero inteiro: "))
cont = 0
if (num > 0):
    for i in range(num):
        for j in range(i+1):
            cont += 1
            print(cont, " ", end="")
        print()