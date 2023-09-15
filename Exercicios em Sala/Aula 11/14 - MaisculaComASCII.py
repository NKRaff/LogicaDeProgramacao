palavra1 = str(input("Digite uma palavra: "))
maiuscula = ""

for i in range(len(palavra1)):
    if (ord(palavra1[i]) >= 97 and ord(palavra1[i]) <= 122): 
        maiuscula += chr(ord(palavra1[i])-32)
    else: maiuscula += palavra1[i]
    
print(f"Maiuscula: {maiuscula}")