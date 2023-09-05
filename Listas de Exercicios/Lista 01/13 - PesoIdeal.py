altura = float(input("Altura(Kg): "))
sexo = str(input("Sexo(M/F): ")).upper()
if(sexo == "M"):
    print(f"Peso Ideal: {(72.7 * altura)-58:.2f}kg")
elif(sexo == "F"):
    print(f"Peso Ideal: {(62.1 * altura)-44.7:.2f}kg")
else:
    print("Sexo Invalido!")