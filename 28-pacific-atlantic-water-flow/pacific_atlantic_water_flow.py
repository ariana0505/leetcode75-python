heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

filas = len(heights)
columnas = len(heights[0])
pacifico = set()
atlantico = set()

def dfs(r, c, visitados):
    if (r, c) in visitados:
        return

    visitados.add((r, c))
    pila = [(r, c)]

    while pila:
        fila, columna = pila.pop()

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = fila + dr, columna + dc
            if nr < 0 or nr >= filas or nc < 0 or nc >= columnas:
                continue
            if (nr, nc) in visitados:
                continue
            if heights[nr][nc] < heights[fila][columna]:
                continue

            visitados.add((nr, nc))
            pila.append((nr, nc))

for r in range(filas):
    dfs(r, 0, pacifico)
    dfs(r, columnas - 1, atlantico)

for c in range(columnas):
    dfs(0, c, pacifico)
    dfs(filas - 1, c, atlantico)

resultado = []
for r in range(filas):
    for c in range(columnas):
        if (r, c) in pacifico and (r, c) in atlantico:
            resultado.append([r, c])

print(resultado)
