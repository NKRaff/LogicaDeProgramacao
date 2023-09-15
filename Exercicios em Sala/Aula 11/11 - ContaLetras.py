texto = (input("Digite uma string: "))

for letra in texto:
    cont = texto.count(letra)
    if cont != 0:
        print(f"{letra}: {cont}x")
        texto = texto.replace(letra,"")

print(texto)
