idade = []
altura = []
mediaAltura = 0
alturaInferior = 0

cont = 1
while(True):
    print(f"{cont}º Aluno: ")

    aux = int(input("Idade: "))
    idade.append(aux)
    if(aux < 0):
        break

    aux = float(input("Altura: "))
    if(aux < 0):
        break
    altura.append(aux)

    mediaAltura += aux
    cont += 1
    print()
mediaAltura /= len(idade)

for i in range(len(idade)):
    if (idade[i] > 13):
        if (altura[i] < mediaAltura):
            alturaInferior += 1

print(f"\nNº de alunos com altura inferior: {alturaInferior}\n")