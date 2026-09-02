matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

filas = len(matrix)
columnas = len(matrix[0])
for fila in range(filas):
    for columna in range(fila + 1, columnas):
        matrix[fila][columna],matrix[columna][fila] = matrix[columna][fila],matrix[fila][columna]
print(matrix)

for fila in range(filas):
    matrix[fila].reverse()
print(matrix)
