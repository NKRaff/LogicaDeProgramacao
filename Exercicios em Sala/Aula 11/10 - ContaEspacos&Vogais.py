texto = str(input("Digite um texto: ")).lower()

espaços = texto.count(" ")
a = texto.count("a")
e = texto.count("e")
i = texto.count("i")
o = texto.count("o")
u = texto.count("u")

print(f"""
Espaços = {espaços}
A = {a}
E = {e}
I = {i}
O = {o}
U = {u}
""")