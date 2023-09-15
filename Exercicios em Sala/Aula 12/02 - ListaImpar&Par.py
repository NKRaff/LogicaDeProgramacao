impar = []
par = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º numero: "))
    if(num % 2 == 0): par.append(num)
    else: impar.append(num)

print(f"""
Lista Impar: {impar}
Lista Par:   {par}
""")