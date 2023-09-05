soma = 0
cont = 0
for i in range(10):
    num = int(input(f"Digite o {i+1}º numero inteiro: "))
    if(num > 0):
        soma += num
        cont += 1
print(f"Media = {soma/cont}")