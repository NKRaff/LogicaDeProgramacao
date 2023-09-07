texto1 = str(input("Digite um texto: "))
texto2 = str(input("Digite mais um texto: "))

print(f"Conteúdo: {texto1}, Tamanho: {len(texto1)}")
print(f"Conteúdo: {texto2}, Tamanho: {len(texto2)}")

if(len(texto1) == len(texto2)):
    print("As duas strings tem o mesmo tamanho!")
if(texto1 == texto2):
    print("As duas strings tem o mesmo conteudo")

