# Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
# M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
# "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("""Maturino(M)
Vesperiano(V)
Noturno(N)""")

turno = str(input("Digite o turno que você estuda: ")).upper()

if(turno == "M"): print("Bom dia!")
elif(turno == "V"): print("Boa tarde!")
elif(turno == "N"): print("Boa noite!")
else: print("Valor Invalido")