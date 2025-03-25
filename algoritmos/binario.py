import math
from cmath import log10
def converter(x):
    xbin = ""
    lista = []
    for i in range (int(math.log2(x)),-1,-1):
        if x - 2**i >= 0:
            lista.append("1")
            x -= 2**i
        else:
            lista.append("0")

    for j in range (len(lista)):
        xbin += lista[j]
    return xbin

def add_binary(a,b):
    x = a+b
    return converter(x)








