idade = []
altura = []
mediaAltura = 0
alturaInferior = 0

for i in range(4):
    print(f"{i+1}º Aluno: ")
    idade.append(int(input("Idade: ")))
    altura.append(float(input("Altura: ")))
    mediaAltura += altura[i]
    print()
mediaAltura /= 4

for i in range(4):
    if (idade[i] > 13):
        if (altura[i] < mediaAltura):
            alturaInferior += 1

print(f"Nº de alunos com altura inferior: {alturaInferior}\n")