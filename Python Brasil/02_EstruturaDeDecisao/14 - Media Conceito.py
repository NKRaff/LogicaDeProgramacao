# Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
# disciplina ao longo de um semestre, e calcule a sua média. A atribuição 
# de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   a) Entre 9.0 e 10.0        A
#   b) Entre 7.5 e 9.0         B
#   c) Entre 6.0 e 7.5         C
#   d) Entre 4.0 e 6.0         D
#   e) Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
# a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o 
# conceito for D ou E.

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
media = (nota1 + nota2)/2

if(media < 4):
    print(f"""
REPROVADO!
1ª Nota = {nota1}
2ª Nota = {nota2}
Media = {media}
Conceito: E
""")

elif(media < 6):
    print(f"""
REPROVADO!
1ª Nota = {nota1}
2ª Nota = {nota2}
Media = {media}
Conceito: D
""")

elif(media < 7.5):
    print(f"""
APROVADO!
1ª Nota = {nota1}
2ª Nota = {nota2}
Media = {media}
Conceito: C
""")
    
elif(media < 9):
    print(f"""
APROVADO!
1ª Nota = {nota1}
2ª Nota = {nota2}
Media = {media}
Conceito: B
""")
    
else:
    print(f"""
APROVADO!
1ª Nota = {nota1}
2ª Nota = {nota2}
Media = {media}
Conceito: A
""")