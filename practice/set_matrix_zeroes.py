matrix = [[1,1,1],[1,0,1],[1,1,1]]
filas = len(matrix)
columnas = len(matrix[0])

filas_z = set()
columnas_z = set()

for fila in range(filas):
    for columna in range(columnas):
        if matrix[fila][columna] == 0:
            filas_z.add(fila)
            columnas_z.add(columna)

for fila in range(filas):
    for columna in range(columnas):
        if fila in filas_z or columna in columnas_z:
            matrix[fila][columna] = 0
