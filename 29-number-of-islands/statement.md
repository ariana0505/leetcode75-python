# 29. Number of Islands / Numero de Islas

## English

Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

### Examples

#### Example 1
```text
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

#### Example 2
```text
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

### Constraints

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.

---

## Espanol

Dada una cuadricula binaria 2D `grid` de tamano `m x n` que representa un mapa de `'1'` (tierra) y `'0'` (agua), devuelve el numero de islas.

Una isla esta rodeada de agua y se forma conectando tierras adyacentes de forma horizontal o vertical. Puedes asumir que los cuatro bordes de la cuadricula estan rodeados de agua.

### Ejemplos

#### Ejemplo 1
```text
Entrada: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Salida: 1
```

#### Ejemplo 2
```text
Entrada: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Salida: 3
```

### Restricciones

- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] es '0' o '1'.
