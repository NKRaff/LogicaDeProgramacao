nome = str(input("Digite seu nome: ")).upper()
for i in range(len(nome)):
    print(nome[-i-1], end="")

# Outra solução
# print(nome[::-1])
