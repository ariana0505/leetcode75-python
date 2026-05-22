# 18. Longest Common Subsequence / Subsecuencia Comun Mas Larga

## English

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A common subsequence of two strings is a subsequence that is common to both strings.

### Examples

#### Example 1
```text
Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

#### Example 2
```text
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

#### Example 3
```text
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

### Constraints

- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.

---

## Espanol

Dadas dos cadenas `text1` y `text2`, devuelve la longitud de su subsecuencia comun mas larga. Si no hay subsecuencia comun, devuelve `0`.

Una subsecuencia de una cadena es una nueva cadena generada a partir de la original eliminando algunos caracteres (posiblemente ninguno) sin cambiar el orden relativo de los caracteres restantes.

- Por ejemplo, `"ace"` es una subsecuencia de `"abcde"`.

Una subsecuencia comun de dos cadenas es una subsecuencia comun a ambas.

### Ejemplos

#### Ejemplo 1
```text
Entrada: text1 = "abcde", text2 = "ace"
Salida: 3
Explicacion: La subsecuencia comun mas larga es "ace" y su longitud es 3.
```

#### Ejemplo 2
```text
Entrada: text1 = "abc", text2 = "abc"
Salida: 3
Explicacion: La subsecuencia comun mas larga es "abc" y su longitud es 3.
```

#### Ejemplo 3
```text
Entrada: text1 = "abc", text2 = "def"
Salida: 0
Explicacion: No existe una subsecuencia comun, asi que el resultado es 0.
```

### Restricciones

- 1 <= text1.length, text2.length <= 1000
- text1 y text2 contienen solo letras minusculas del ingles.
