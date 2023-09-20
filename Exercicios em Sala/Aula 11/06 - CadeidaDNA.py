dna = str(input("Digite a cadeia de DNA: ")).upper().replace(" ", "")
dnaComplementar = ""

for i in range(len(dna)):
    if(dna[i] == "A"): dnaComplementar += "T"
    elif(dna[i] == "T"): dnaComplementar += "A"
    elif(dna[i] == "C"): dnaComplementar += "G"
    elif(dna[i] == "G"): dnaComplementar += "C"

print(f"DNA Complementar: {dnaComplementar}")