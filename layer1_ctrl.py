import numpy as np



n_stages = 3 # log2 ( numero de p o nt o s )
N =int(2**n_stages) # numero de p o nt o s
valores = np.zeros([n_stages, N])
cnt = 0
for i in range(n_stages):
    b = []
    cnt = 0
    for j in range(N):
        if j not in b :
            valores[i][j] = cnt
            valores[i][j + 2**i] = valores[i][j]
            b.append(j + 2**i)
            b.append(j)
            cnt += 1

for i in range(n_stages-1):
    step = int(N/(2**(n_stages-1-i)))
    for k in range(int(N/step)-1):

        valores[i][(k+1)* step : (k +1)* step + step] = valores[i][k*step: k*step + step] + step
        print((k+1)* step,' ', (k +1)* step + step, ' ',k*step,' ', k*step+ step)
    print("Novo K ")
print(valores)


