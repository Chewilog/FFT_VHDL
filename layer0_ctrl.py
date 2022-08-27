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

print("constant layer0_vals:ctr0_array :=",end='')
print("(",end='')
for i in w:
    print('(',end='')
    for j in range(len(i)):
        if j ==len(i)-1:
            print(i[j],end='')
        else:
            print(i[j],end=',')
    print(')',end='')
print(');')