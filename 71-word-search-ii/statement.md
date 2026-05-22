# 71. Word Search II / Busqueda de Palabra II

## English

Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

### Examples

#### Example 1
```text
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

#### Example 2
```text
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
```

### Constraints

- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] is a lowercase English letter.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] consists of lowercase English letters.
- All the strings of words are unique.

---

## Espanol

Dada una cuadricula `board` de caracteres de `m x n` y una lista de cadenas `words`, devuelve todas las palabras que aparecen en la cuadricula.

Cada palabra debe construirse con letras de celdas adyacentes en secuencia, donde las celdas adyacentes son vecinas horizontal o verticalmente. La misma celda no se puede usar mas de una vez en una palabra.

### Ejemplos

#### Ejemplo 1
```text
Entrada: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
         words = ["oath","pea","eat","rain"]
Salida: ["eat","oath"]
```

#### Ejemplo 2
```text
Entrada: board = [["a","b"],["c","d"]], words = ["abcb"]
Salida: []
```

### Restricciones

- m == board.length
- n == board[i].length
- 1 <= m, n <= 12
- board[i][j] es una letra minuscula del ingles.
- 1 <= words.length <= 3 * 10^4
- 1 <= words[i].length <= 10
- words[i] contiene solo letras minusculas del ingles.
- Todas las cadenas de words son unicas.
