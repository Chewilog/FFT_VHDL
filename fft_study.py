import numpy as np
import struct
import matplotlib.pyplot as plt

m = 10

N=2**m  # Tamanho da FFT
N_conj = 128 # número de conjuntos de amostras gerados
max_in = 20.0  # input_máximo


conjunto_amostras = []
resultados = []
np.random.seed(180126083)

def float2bin(a,b,num):
    binrep = ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
    h = binrep[0:a+b+1]
    return h


for i in range(N_conj):
        amostras = 2*max_in*(np.random.rand(1,N)-0.5)
        conjunto_amostras.append(amostras)

conjunto_amostras = np.array(conjunto_amostras)
for i in conjunto_amostras:
    resultados.append(np.fft.fft(i)[0])                   #FFT propriamente dita

resultados = np.array(resultados)


print('\namostras------------------------------------------------\n')

print(conjunto_amostras)

print('\nresultados------------------------------------------------\n')
print(resultados)

# plt.title('Amostras')
# plt.plot(conjunto_amostras[0][0])
# plt.show()
#
# plt.title('Resultados(módulo)')
# plt.plot(np.abs(resultados[0]))
# plt.show()