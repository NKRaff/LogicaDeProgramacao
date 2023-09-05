nota1 = float(input("Digite a 1ª nota: "))
if (nota1 >= 0 and nota1 <= 10):
    nota2 = float(input("Digite a 2ª nota: "))
    if (nota2 >= 0 and nota2 <= 10):
        print(f"Media: {((nota1 + nota2) / 2):.2f}")
    else: print("Nota Invalida!")
else: print("Nota Invalida!")