matrix = [[1,1,1],[1,0,1],[1,1,1]]

# Primero obtenemos las dimensiones para poder recorrer toda la matriz.
filas = len(matrix)
columnas = len(matrix[0])

# Guardamos por separado las filas y columnas que contienen un cero original.
filas_zero = set()
columnas_zero = set()

# En el primer recorrido solo registramos posiciones; todavía no modificamos la matriz.
for fila in range(filas):
    for columna in range(columnas):
        if matrix[fila][columna] == 0:
            filas_zero.add(fila)
            columnas_zero.add(columna)

# En el segundo recorrido ponemos a cero cada celda cuya fila o columna fue marcada.
for fila in range(filas):
    for columna in range(columnas):
        if fila in filas_zero or columna in columnas_zero:
            matrix[fila][columna] = 0

# Mostramos la matriz una vez aplicadas todas las marcas.
print(matrix)
