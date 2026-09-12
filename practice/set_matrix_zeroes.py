matrix = [[1,1,1],[1,0,1],[1,1,1]]
filas = len(matrix)
columnas = len(matrix[0])

filas_zero = set()
columnas_zero = set()

for fila in range(filas):
    for columna in range(columnas):
        if matrix[fila][columna] == 0:
            filas_zero.add(fila)
            columnas_zero.add(columna)

for fila in range(filas):
    for columna in range(columnas):
        if fila in filas_zero or columna in columnas_zero:
            matrix[fila][columna] = 0

print(matrix)
