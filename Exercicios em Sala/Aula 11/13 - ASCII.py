palavra1 = str(input("Digite um palavra: "))
palavra2 = ""

for i in palavra1:
    aux = ord(i)
    print(aux)
    aux += 1
    palavra2 += chr(aux)

print(f"Nava palavra ASCII: {palavra2}")