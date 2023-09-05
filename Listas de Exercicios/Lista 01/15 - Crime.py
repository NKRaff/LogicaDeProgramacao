print("Responda apenas com: Sim / Não")
classificacao = 0

pergunta = str(input("Telefonou para a vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Esteve no local do crime? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Mora perto da vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Devia para a vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

pergunta = str(input("Já trabalhou com a vítima? ")).lower()
if(pergunta == "sim"): classificacao += 1

if (classificacao == 5): print("Assassino")
elif (classificacao == 4 or classificacao == 3): print("Cúmplice")
elif (classificacao == 2): print("Suspeita")
else: print("Inocente")