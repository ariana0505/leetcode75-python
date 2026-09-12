matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# Primero obtenemos las dimensiones para recorrer toda la matriz.
filas = len(matrix)
columnas = len(matrix[0])

# Intercambiamos los elementos sobre la diagonal para transponer la matriz.
for fila in range(filas):
    # Empezamos después de la diagonal para no repetir intercambios.
    for columna in range(fila + 1, columnas):
        matrix[fila][columna],matrix[columna][fila] = matrix[columna][fila],matrix[fila][columna]
print(matrix)

# Finalmente invertimos cada fila; así completamos el giro de 90 grados.
for fila in range(filas):
    matrix[fila].reverse()
print(matrix)
