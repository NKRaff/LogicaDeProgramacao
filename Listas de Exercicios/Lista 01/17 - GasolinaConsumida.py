distancia = float(input("Digite a distância(Km): "))
litros = float(input("Digite a quantidade de gasolina consumida(l): "))
kml = distancia / litros
if (kml < 8): print("Venda o carro!")
elif (kml <= 12): print("Econômico!")
else: print("Super econômico!")