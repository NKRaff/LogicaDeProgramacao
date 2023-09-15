palavra1 = str(input("Digite uma palavra: "))
maiuscula = ""

for i in range(len(palavra1)):
    aux = ord(palavra1[i])
    if (aux >= 97 and aux <= 122):
        aux -= 32
    maiuscula += chr(aux)

print(f"Maiuscula: {maiuscula}")