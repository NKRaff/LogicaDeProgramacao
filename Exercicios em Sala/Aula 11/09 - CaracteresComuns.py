texto1 = str(input("Digite um texto: "))
texto2 = str(input("Digite um texto: "))
iguais = ""

for i in texto1:
    for j in texto2:
        if j == i:
            iguais += j

print(f"Letras Iguais: {iguais}")
