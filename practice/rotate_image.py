matrix = [[1,2,3],[4,5,6],[7,8,9]]

filas = len(matrix)
columnas = len(matrix[0])

for fila in range(filas):
    for columna in range(fila + 1,columnas):
        matrix[columna][fila],matrix[fila][columna] = matrix[fila][columna],matrix[columna][fila]

for fila in matrix:
    fila.reverse()