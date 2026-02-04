## Word Search (English)

Given an `m x n` grid of characters `board` and a string `word`, return `true` if the word exists in the grid.

The word can be constructed from letters of **sequentially adjacent cells**, where adjacent cells are **horizontally or vertically neighboring**.  
The same letter cell **may not be used more than once**.

### Example 1
**Input:**  
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "ABCCED"`  

**Output:** `true`

### Example 2
**Input:**  
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "SEE"`  

**Output:** `true`

### Example 3
**Input:**  
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "ABCB"`  

**Output:** `false`

### Constraints
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` and `word` consist only of **uppercase and lowercase English letters**

---

## Búsqueda de Palabras (Español)

Dada una cuadrícula de caracteres `board` de tamaño `m x n` y una cadena `word`, devuelve `true` si la palabra existe en la cuadrícula.

La palabra puede construirse a partir de letras de **celdas adyacentes de forma secuencial**, donde las celdas adyacentes son **vecinas horizontal o verticalmente**.  
Una misma celda **no puede usarse más de una vez**.

### Ejemplo 1
**Entrada:**  
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "ABCCED"`  

**Salida:** `true`

### Ejemplo 2
**Entrada:**  
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "SEE"`  

**Salida:** `true`

### Ejemplo 3
**Entrada:**  
`board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`  
`word = "ABCB"`  

**Salida:** `false`

### Restricciones
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`
- `board` y `word` contienen solo **letras mayúsculas y minúsculas del alfabeto inglés**
