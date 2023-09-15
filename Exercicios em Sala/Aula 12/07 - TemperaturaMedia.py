mesPorExtenso = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

temperaturaAnual = 0
temperaturaMes = []

print("Digite a temperatura media do")

for i in range(12):
    temperaturaMes.append(float(input(f"{i+1}º Mês: ")))
    temperaturaAnual += temperaturaMes[i]

print()
for i in range(len(temperaturaMes)):
    print(f"{mesPorExtenso[i]} = {temperaturaMes[i]}°C")
print(f"Media do Ano: {(temperaturaAnual/12):.2f}°C")