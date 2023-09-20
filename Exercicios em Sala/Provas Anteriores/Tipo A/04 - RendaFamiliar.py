familias = []
contadorDeFamilias = 0

# Loop para adição de familias
while(True):
    # Inicialização/Entrada de variaveis
    contadorDeFamilias += 1
    rendaTotal = 0
    print(f"\n| Família {contadorDeFamilias} |")
    numeroDePessoas = int(input("Digite o número de pessoas na familia: "))
    
    # Adiciona lista de pessoas a lista de familias
    renda = []
    for i in range(numeroDePessoas):
        rendaAux = float(input(f"Digite a renda da {i+1}ª Pessoa: R$"))
        renda.append(rendaAux)
        rendaTotal += rendaAux
    familias.append(renda)
    rendaMedia = rendaTotal / numeroDePessoas

    # Print de informações da familia
    print(f"""
Nº de pessoas: {numeroDePessoas}
Renda Total: R${rendaTotal:.2f}
Renda Media: R${rendaMedia:.2f}
""")
    
    # Condição para continuar adicionar familias
    continuar = str(input("Ainda há famílias? (sim para continuar)\n"))
    if (continuar != "sim"): break
# Fim do while

# Calculo para: 
rendaMediaCidade = 0
familiaComRendaSuperior = 0
familiaComRendaInferior = 0

for pessoa in familias:
    rendaFamilia = 0
    # Renda familiar media
    for renda in pessoa:
        rendaMediaCidade += renda
        rendaFamilia += renda

    # Percentual de familia com - de 1 salario minimo
    if (rendaFamilia < 1212): familiaComRendaInferior+=1
    # Quantidade de familia com 10/+ salarios
    if (rendaFamilia >= 1212*10): familiaComRendaSuperior+=1

print(f"""
Renda familiar media da cidade: R${(rendaMediaCidade / contadorDeFamilias):.2f}
Percentual de Familia com menos de 1 salario: {(familiaComRendaInferior * 100 / contadorDeFamilias):.2f}%
Nº de familias com 10 ou mais salarios: {familiaComRendaSuperior}
""")
