# 45. Set Matrix Zeroes / Poner en Cero la Matriz

## English

Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s.

You must do it in place.

### Examples

#### Example 1
```text
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```

#### Example 2
```text
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

### Constraints

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

---

## Espanol

Dada una matriz de enteros `matrix` de `m x n`, si un elemento es `0`, pon toda su fila y columna en `0`.

Debes hacerlo in place (sin usar una matriz extra completa).

### Ejemplos

#### Ejemplo 1
```text
Entrada: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Salida: [[1,0,1],[0,0,0],[1,0,1]]
```

#### Ejemplo 2
```text
Entrada: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Salida: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

### Restricciones

- m == matrix.length
- n == matrix[0].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1
