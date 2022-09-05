import numpy as np
import struct

N=8
N_ram = 2048
inc=int(N_ram/N)

valores_real = np.zeros(N_ram)
valores_imag = np.zeros(N_ram)
valores = np.zeros(N_ram,dtype=np.complex_)
i =np.complex(0,1)


def float2bin(a,b,num):
    binrep = ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))
    h = binrep[0:a+b+1]
    return h


imag_rom = open("imag_rom"+'.coe','w')
real_rom = open("real_rom"+'.coe','w')

imag_rom.write("memory_initialization_radix=2;\nmemory_initialization_vector=\n")
real_rom.write("memory_initialization_radix=2;\nmemory_initialization_vector=\n")

for j in range(N_ram):
    valores[j] = np.e**(-2*np.pi*i*j/N_ram)
    print(valores[j])
    if j == N_ram-1:
        real_rom.write(float2bin(8,18,np.real(valores[j]))+';')
        imag_rom.write(float2bin(8,18,np.imag(valores[j]))+';')
        continue
    real_rom.write(float2bin(8,18,np.real(valores[j]))+',\n')
    imag_rom.write(float2bin(8,18,np.imag(valores[j]))+',\n')





