while (True):
    nome = str(input("Digite o nome do atleta: "))
    if(nome == ""): break
    
    saltos = []
    media = 0
    
    for i in range(5):
        saltos.append(float(input(f"{i+1}º Salto: ")))
        media += saltos[i]
    
    print(f"""\nResultado final
Atleta: {nome}
Saltos: {saltos[0]} - {saltos[1]} - {saltos[2]} - {saltos[3]} - {saltos[4]}
Média dos saltos: {media/5} m
""")

    saltos.clear()
