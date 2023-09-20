texto = str(input("Digite um texto: ")).lower()

print(f"""
Espaços = {texto.count(" ")}
A = {texto.count("a")}
E = {texto.count("e")}
I = {texto.count("i")}
O = {texto.count("o")}
U = {texto.count("u")}
""")