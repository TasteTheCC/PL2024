file = "emd.csv"

with open(file, "r") as f:
    linhas = f.readlines()

    data = []

    for line in linhas[1:]:
        data.append(line.strip().split(","))

fit = 0 # aptidao
sport = []
intervalo1 = []
intervalo2 = []
intervalo3 = []

for field in data: #campos de cada linha

    if (field[12] == "true"):
        fit += 1

    if field[8] not in sport:
        sport.append(field[8])
    
    idade = int(field[5])

    if 30 <= idade <= 34:
        intervalo1.append(field[0])

    elif 35 <= idade <= 39:
        intervalo2.append(field[0])

    elif 40 <= idade <= 44:
        intervalo3.append(field[0])

sport.sort() # ordenar alfabeticamente as modalidades

percentagem = fit * 100 / len(data)

print("-----Pergunta 1-----")
print(f"Modalidades: {sport}\n")

print("-----Pergunta 2-----")
print(f"% atletas aptos: {percentagem}\n")
print(f"% atletas inaptos: {100 - percentagem}\n")

print("-----Pergunta 3-----")
print(f"Atletas na faixa etária 1 [30-34]: {escalao1}\n")
print(f"Atletas na faixa etária 2 [35-39]: {escalao2}\n")
print(f"Atletas na faixa etária 3 [40-44]: {escalao3}\n")