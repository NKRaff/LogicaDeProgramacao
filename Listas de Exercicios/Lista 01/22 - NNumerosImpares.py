num = int(input("Digite um numero inteiro: "))
i = 0
while(num!=0):
    i += 1
    if(i % 2 != 0): 
        print(i, " ", end="")
        num -= 1