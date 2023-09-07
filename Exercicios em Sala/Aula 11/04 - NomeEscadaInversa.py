nome = str(input("Digite seu nome: "))

for i in range(len(nome), 0, -1):
    for j in range(i):
        print(nome[j], end="")
    print()
