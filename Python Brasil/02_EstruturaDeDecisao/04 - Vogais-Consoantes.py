# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: "))

if(letra == "a" or 
   letra == "e" or
   letra == "i" or
   letra == "o" or
   letra == "u"):
    print(f"A letra {letra} é uma vogal")
elif(len(letra) == 0):
    print("Erro! Nenhuma letra digitada")
elif(len(letra) > 1):
    print("Erro! Mais de uma letra digitada")
else:
    print(f"A letra {letra} é uma consoante")
