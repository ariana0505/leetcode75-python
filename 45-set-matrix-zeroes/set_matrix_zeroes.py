matrix = [[1,1,1],[1,0,1],[1,1,1]]

filas = set()
columnas = set()

for fila in range(len(matrix)):
    for columna in range(len(matrix[0])):
        if matrix[fila][columna] == 0:
            filas.add(fila)
            columnas.add(columna)
for fila in range(len(matrix)):
    for columna in range(len(matrix[0])):
        if fila in filas or columna in columnas :
            matrix[fila][columna] = 0

print(matrix)
