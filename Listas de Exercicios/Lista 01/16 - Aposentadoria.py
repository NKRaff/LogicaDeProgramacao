idade = int(input("Digite sua idade: "))
tempo = float(input("Tempo de serviço: "))

if(idade >= 65): print("Pode se Aposentar")
elif (tempo >= 30): print("Pode se Aposentar")
elif (idade >= 60 and tempo >= 25): print("Pode se Aposentar")
else: print("Não pode se Aposentar")