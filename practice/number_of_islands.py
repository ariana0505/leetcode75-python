grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
filas = len(grid)
columnas = len(grid[0])
islas = 0

def number_of_islands(fila, columna):
    if fila< 0 or columna < 0 or fila >= filas or columna >= columnas or grid[fila][columna] != "1":
        return
    grid[fila][columna] = "0"
    number_of_islands(fila + 1,columna)
    number_of_islands(fila - 1,columna)
    number_of_islands(fila,columna + 1)
    number_of_islands(fila,columna - 1)

for fila in range(filas):
    for columna in range(columnas):
        if grid[fila][columna] == "1":
            islas += 1
            number_of_islands(fila,columna)

print(islas)