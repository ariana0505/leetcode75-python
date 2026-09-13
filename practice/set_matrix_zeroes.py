matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
filas = len(matrix)
columnas = len(matrix[0])

filas_zeros = set()
columnas_zeros = set()

for fila in range(filas):
    for columna in range(columnas):
        if matrix[fila][columna] == 0 :
            filas_zeros.add(fila)
            columnas_zeros.add(columna)

for fila in range(filas):
    for columna in range(columnas):
        if fila in filas_zeros or columna in columnas_zeros:
            matrix[fila][columna] = 0

