# file = open("x.txt","r")
#
# for line in file.readlines():
#     print(int((line[0:-1].encode()),2),end='-')
import numpy as np
import struct



def float2bin(a,b,num):
    binrep = ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
    h = binrep[0:a+b+1]
    return h

files_dict = {}
xs = []

N = 8
num_in = 1
max_in = 20.0

np.random.seed(180126083)
w = 2*(np.random.rand(1,num_in)-0.5)
bias = 2*(np.random.rand()-0.5)



for i in range(num_in):
    files_dict[i] = open('x'+str(i)+'.txt','w')
    # files_dict[i].write("memory_initialization_radix=2;\nmemory_initialization_vector=\n")

for i in range(num_in):
    xs.append([])
    for j in range(N):
        xs[i].append(max_in*(np.random.rand()-0.5))
        if j == N-1:
            files_dict[i].write(float2bin(8, 18, xs[i][j])+'')
            continue
        files_dict[i].write(float2bin(8, 18, xs[i][j])+'\n')

print(xs)

filefx = open('filefx.txt','w')
Xs = np.fft.fft(xs[0][::-1])
for i in Xs:
    filefx.write(str(i)+"\n")








# v = w[0][0]*xs[0][0]+ w[0][1]*xs[1][0]+ w[0][2]*xs[2][0]+ w[0][3]*xs[3][0] + bias
# print(v,str(1/(1+np.exp(-v))))
#
# v=0
# for j in range(N):
#     for i in range(num_in):
#         v += xs[i][j]*w[0][i]
#     v+=bias
#     filefx.write(str(1/(1+np.exp(-v)))+'\n')
#     v=0
#
#
# for i in w[0]:
#     print('w=',float2bin(8,18,i),'------',i)
#
# print("bias=",float2bin(8,18,bias),"------",bias)