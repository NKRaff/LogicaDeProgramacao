import os
os.system('cls')

metrosQuadrados = float(input("Digite o metro quadrado: "))
litros = metrosQuadrados / 3
litrosTotais = litros
latas = 0

while(litros >= 18):
    latas += 1
    litros -= 18

if(litros != 0):
    latas += 1

preco = latas * 80

print("Latas: {}".format(latas))
print("Litros: {:.2f}".format(litrosTotais))
print("Preço: R${:.2f}".format(preco))
