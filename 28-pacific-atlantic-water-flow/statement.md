# 28. Pacific Atlantic Water Flow / Flujo de Agua Pacifico Atlantico

## English

There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into that ocean.

Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

### Examples

#### Example 1
```text
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

#### Example 2
```text
Input: heights = [[1]]
Output: [[0,0]]
```

### Constraints

- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5

---

## Espanol

Hay una isla rectangular de `m x n` que limita con el Oceano Pacifico y el Oceano Atlantico. El Oceano Pacifico toca los bordes izquierdo y superior de la isla, y el Oceano Atlantico toca los bordes derecho e inferior de la isla.

Se te da una matriz de enteros `heights` de `m x n` donde `heights[r][c]` representa la altura sobre el nivel del mar de la celda en la coordenada `(r, c)`.

La isla recibe mucha lluvia, y el agua de lluvia puede fluir a celdas vecinas directamente al norte, sur, este y oeste si la altura de la celda vecina es menor o igual a la altura de la celda actual. El agua puede fluir desde cualquier celda adyacente a un oceano hacia ese oceano.

Devuelve una lista 2D de coordenadas de la cuadricula `result` donde `result[i] = [ri, ci]` indica que el agua de lluvia puede fluir desde la celda `(ri, ci)` hacia ambos oceanos, el Pacifico y el Atlantico.

### Ejemplos

#### Ejemplo 1
```text
Entrada: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Salida: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
```

#### Ejemplo 2
```text
Entrada: heights = [[1]]
Salida: [[0,0]]
```

### Restricciones

- m == heights.length
- n == heights[r].length
- 1 <= m, n <= 200
- 0 <= heights[r][c] <= 10^5
