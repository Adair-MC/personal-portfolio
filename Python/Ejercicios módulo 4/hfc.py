# Histograma de frecuencia de caracteres
# --------------------------------------
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
    for ch in counters.keys():
        c = counters[ch]
        if c > 0:
            print(ch, '->', c)
except IOError:
    print("Error: ", strerror(IOError.errno))
