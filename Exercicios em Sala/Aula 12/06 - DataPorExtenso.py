mes = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

data = str(input("Digite a data de nascimento (dd/mm/aaaa):\n")).split("/")
print(f"Você nasceu em {data[0]} de {mes[int(data[1])-1]} de {data[2]}")