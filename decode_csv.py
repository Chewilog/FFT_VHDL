import csv
import struct
from codecs import decode
from ctypes import *
import numpy as np
import matplotlib.pyplot as plt

libc = CDLL('msvcrt')


def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]



saidas = []
with open('iladata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if row[2] == '1':
            for i in range(3,19,1):
                print(bin_to_float(row[i] + "00000"))
            # saidas.append(bin_to_float(row[5] + "00000"))