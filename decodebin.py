import struct


def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

resultados = open("F.txt",'r')




for line in resultados.readlines():
    for j in line.split(','):
        print(bin_to_float(j+"00000"))
