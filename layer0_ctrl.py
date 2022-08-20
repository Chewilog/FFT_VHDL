m = 3
N = 2**m  # numero de pontos

stages = m
w = []

for i in range(stages):
    aux =[]
    for j in range(int(N)):
        if j & 2**i:
            aux.append(j)

    w.append(aux)

print(w)