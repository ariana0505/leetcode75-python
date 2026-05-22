# 48. Word Search / Busqueda de Palabra

## English

Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### Examples

#### Example 1
```text
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

#### Example 2
```text
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

#### Example 3
```text
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

### Constraints

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

---

## Espanol

Dada una cuadricula de caracteres `board` de `m x n` y una cadena `word`, devuelve `true` si `word` existe en la cuadricula.

La palabra se puede construir con letras de celdas adyacentes en secuencia, donde las celdas adyacentes son vecinas horizontal o verticalmente. La misma celda no se puede usar mas de una vez.

### Ejemplos

#### Ejemplo 1
```text
Entrada: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Salida: true
```

#### Ejemplo 2
```text
Entrada: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Salida: true
```

#### Ejemplo 3
```text
Entrada: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Salida: false
```

### Restricciones

- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board y word contienen solo letras minusculas y mayusculas del ingles.
