palavra1 = str(input("Digite um palavra: "))
palavra2 = ""

for i in palavra1:
    aux = ord(i)
    aux += 1
    palavra2 += chr(aux)
    # palavra2 += chr(ord(i)+1)

print(f"Nava palavra ASCII: {palavra2}")