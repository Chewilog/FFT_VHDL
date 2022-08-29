m = 3
N = 2**m  # numero de pontos

stages = m
w = []

def modulo(a, b):
    return a-int(a/b)*b

for i in range(stages):
    aux =[]
    for j in range(int(N/2)):
            aux.append(modulo(j, 2**i)*2**(stages-i-1))
    w.append(aux)


print("constant layer0w_vals:wctr0_array_int_full :=",end='')
print("(",end='')
for i in w:
    print('(',end='')
    for j in range(len(i)):
        if j ==len(i)-1:
            print(i[j],end='')
        else:
            print(i[j],end=',')
    print(')',end=',')
print(');')

