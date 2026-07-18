"""
NUMBER OF ISLANDS con BFS (recorrido en anchura)
=================================================

Una matriz de "1" (tierra) y "0" (agua). Una "isla" es un grupo de "1"
conectados en horizontal o vertical. Hay que contar cuántas islas hay.

La matriz ES un grafo:
  - cada celda es un NODO
  - cada celda tiene hasta 4 VECINOS: arriba, abajo, izquierda, derecha
    (NO en diagonal)

Contar islas = contar cuántos "componentes conexos" de tierra hay.

IDEA:
  Recorremos toda la matriz. Cuando encontramos un "1" que todavía no
  visitamos, es una isla NUEVA -> sumamos 1 al contador y lanzamos un BFS
  que marca (hunde) TODA esa isla para no volver a contarla.
"""

from collections import deque


def num_islas(grid):
    filas = len(grid)
    columnas = len(grid[0])
    contador = 0

    def pintar_isla(r, c):
        cola = deque()
        cola.append((r, c))
        grid[r][c] = "0"                 # pinto de agua al encolar
        while cola:
            fila, col = cola.popleft()   # saco el primero de la fila (FIFO)
            # miro los 4 vecinos
            for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nf, nc = fila + df, col + dc
                # ¿está dentro del mapa Y es tierra sin visitar?
                if 0 <= nf < filas and 0 <= nc < columnas and grid[nf][nc] == "1":
                    grid[nf][nc] = "0"      # la pinto
                    cola.append((nf, nc))   # la apunto como pendiente

    for r in range(filas):
        for c in range(columnas):
            if grid[r][c] == "1":        # tierra nueva = isla nueva
                contador += 1
                pintar_isla(r, c)        # hundo la isla entera

    return contador


if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(num_islas(grid1))  # 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(num_islas(grid2))  # 3




# ------------------------------------------------------------------
# ¿POR QUÉ FUNCIONA?  (traza mental con grid2)
# ------------------------------------------------------------------
# El doble for recorre celda por celda. Al encontrar el primer "1" (0,0):
#   - contador = 1
#   - BFS arranca en (0,0), lo hunde, y desde la cola va visitando por
#     "anillos": (0,1) y (1,0)  ->  luego (1,1)  -> se vacía la cola.
#     Toda esa isla queda en "0".
# El for sigue avanzando; ya no vuelve a contar esas celdas porque son "0".
# El siguiente "1" que aparezca (2,2) es una isla NUEVA -> contador = 2, etc.
#
# DFS vs BFS aquí:
#   - Ambos "hunden" la isla completa; el RESULTADO es idéntico.
#   - DFS usa recursión (pila) -> más corto de escribir, pero en un grid
#     enorme puede reventar el límite de recursión de Python.
#   - BFS usa una cola explícita -> ocupa memoria pero NO desborda la pila.
#
# Complejidad: O(filas * columnas). Cada celda se encola/visita una sola vez.
