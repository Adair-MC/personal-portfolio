# Histograma de frecuencia de caracteres ordenado
# -----------------------------------------------
# Samuel Melo y Johan Yasno
from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
f_name = input("Ingresa el nombre del archivo: ")
try:
    file = open(f_name, "rt")
    for line in file:
        for ch in line:
            if ch.isalpha():
                counters[ch.lower()] += 1
    file.close()
    file = open(f_name + '.hist', 'wt')
    for ch in sorted(counters.keys(), key=lambda x: counters[x], reverse=True):
        c = counters[ch]
        if c > 0:
            file.write(ch + ' -> ' + str(c) + '\n')
    file.close()
except IOError:
    print("Error: ", strerror(IOError.errno))