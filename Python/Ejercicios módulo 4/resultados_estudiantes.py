# Evaluando los resultados de los estudiantes
# -------------------------------------------
# Samuel Melo y Johan Yasno
class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)

from os import strerror

data = { }

f_name = input("Ingresa el nombre del archivo de datos del estudiante: ")
line_n = 1
try:
    f = open(f_name, "rt")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        raise FileEmpty()
    for i in range(len(lines)):
        line = lines[i]
        columns = line.split()
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        student = columns[0] + ' ' + columns[1]
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError:
    print("Error: ", strerror(IOError.errno))
except WrongLine:
    print("Línea incorrecta #" + str(WrongLine.line_n) + " en el archivo:" + WrongLine.line_string)
except FileEmpty:
    print("Archivo vacío")