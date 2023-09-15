num = int(input("Digite um numero ate 99: "))
aux = num
unidade = ""
dezena = ""

if (num < 100):
    if(num >= 90): aux -= 90; dezena = "noventa"
    elif(num >= 80): aux -= 80; dezena = "oitenta"
    elif(num >= 70): aux -= 70; dezena = "setenta"
    elif(num >= 60): aux -= 60; dezena = "sessenta"
    elif(num >= 50): aux -= 50; dezena = "cinquenta"
    elif(num >= 40): aux -= 40; dezena = "quarenta"
    elif(num >= 30): aux -= 30; dezena = "trinta"
    elif(num >= 20): aux -= 20; dezena = "vinte"
    elif(num == 19): aux -= 19; dezena = "dezenove"
    elif(num == 18): aux -= 18; dezena = "dezeoito"
    elif(num == 17): aux -= 17; dezena = "dezessete"
    elif(num == 16): aux -= 16; dezena = "dezesseis"
    elif(num == 15): aux -= 15; dezena = "quinze"
    elif(num == 14): aux -= 14; dezena = "quatorze"
    elif(num == 13): aux -= 13; dezena = "treze"
    elif(num == 12): aux -= 12; dezena = "doze"
    elif(num == 11): aux -= 11; dezena = "onze"
    elif(num == 10): aux -= 10; dezena = "dez"
    
    if(aux == 9): unidade = "nove"
    elif(aux == 8): unidade = "oito"
    elif(aux == 7): unidade = "sete"
    elif(aux == 6): unidade = "seis"
    elif(aux == 5): unidade = "cinco"
    elif(aux == 4): unidade = "quatro"
    elif(aux == 3): unidade = "três"
    elif(aux == 2): unidade = "dois"
    elif(aux == 1): unidade = "um"

    if(aux == 0):
        print(f"{num} = {dezena}")
    else:
        print(f"{num} = {dezena} e {unidade}")
    