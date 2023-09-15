idade = []
altura = []
mediaAltura = 0
alturaInferior = 0

quantidadeDeAlunos = int(input("Quantidade de Alunos: "))

for i in range(quantidadeDeAlunos):
    print(f"{i+1}º Aluno: ")
    idade.append(int(input("Idade: ")))
    altura.append(float(input("Altura: ")))
    mediaAltura += altura[i]
    print()
mediaAltura /= quantidadeDeAlunos

for i in range(quantidadeDeAlunos):
    if (idade[i] > 13):
        if (altura[i] < mediaAltura):
            alturaInferior += 1

print(f"Nº de alunos com altura inferior: {alturaInferior}\n")