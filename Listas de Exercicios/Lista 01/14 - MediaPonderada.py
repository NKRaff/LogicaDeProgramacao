nota1 = float(input("Digite a 1ª nota: "))
if (nota1 >= 0 and nota1 <= 10):
    nota2 = float(input("Digite a 2ª nota: "))

    if (nota2 >= 0 and nota2 <= 10):
        nota3 = float(input("Digite a 2ª nota: "))

        if (nota3 >= 0 and nota3 <= 10):
            media = (nota1*2 + nota2*3 + nota3*5) / 10
            print(f"Media: {media:.2f}")
            
        else: print("Nota Invalida!")
    else: print("Nota Invalida!")
else: print("Nota Invalida!")