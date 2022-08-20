n_stages = 3 # log2 ( numero de p o nt o s )
N =int(2**n_stages) # numero de p o nt o s

for i in range(n_stages):
    for j in range(N):
        print(2*j*2**i)
        # print((2*j+1)*2**i)
    print("novo estagio")