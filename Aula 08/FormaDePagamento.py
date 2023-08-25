import os
os.system('cls')

preco = float(input("Preço do Produto: "))
codigo = int(input("Codigo de Pagamento: "))
precoTotal = 0

if(codigo == 1):
    precoTotal = preco - preco * 0.1
    print(f"Preço a pagar: R${precoTotal:.2f}")
elif(codigo == 2):
    precoTotal = preco - preco * 0.15
    print(f"Preço a pagar: R${precoTotal:.2f}")
elif(codigo == 3):
    precoTotal = preco / 2
    print(f"Preço a pagar: 2x R${precoTotal:.2f}")
elif(codigo == 4):
    precoTotal = (preco * 1.1)/3
    print(f"Preço a pagar: 3x R${precoTotal:.2f}")
elif(codigo == 5):
    precoTotal = (preco * 1.2)/6
    print(f"Preço a pagar: 6x R${precoTotal:.2f}")
else:
    print("Codigo Invalido!")

