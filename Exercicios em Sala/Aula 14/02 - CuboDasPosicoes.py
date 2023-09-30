lista = []
resultado = []
while(True):
    num = input("Digite um numero: (Qualquer letra para sair): ")
    if num.isnumeric(): lista.append(int(num))
    else: break
for i in lista:
    tupla = (i, i**3) 
    resultado.append(tupla)
print(resultado)