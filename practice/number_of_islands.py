grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

filas = len(grid)
columnas = len(grid[0])
contador = 0

def count(fila,columna):
    if 0> fila or 0> columna or columna >= columnas or fila >= filas or grid[fila][columna] != "1":
        return

    grid[fila][columna] = "0"

    count(fila + 1 , columna)
    count(fila - 1 , columna)
    count(fila , columna + 1)
    count(fila , columna - 1)

for fila in range(filas):
    for columna in range(columnas):
        if grid[fila][columna] == "1":
            count(fila,columna)
            contador += 1

print(contador)
