atual = 1
ultimo = 1
antepenultimo = 0

num = int(input("Digite o numero de séries de Fibonacci: "))

if(num <= 0): print("Termo Invalido!")
elif(num == 1): print(ultimo)
elif(num == 2): print(f"{ultimo}, {atual}")
else:
    print(f"{ultimo}, {atual}", end="")
    for i in range(num-2):
        antepenultimo = ultimo
        ultimo = atual
        atual += antepenultimo
        print(f", {atual}", end="")