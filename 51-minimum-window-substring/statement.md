# 51. Minimum Window Substring / Subcadena de Ventana Minima

## English

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

### Examples

#### Example 1
```text
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

#### Example 2
```text
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

#### Example 3
```text
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
```

### Constraints

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- `s` and `t` consist of uppercase and lowercase English letters.

### Follow-up

Could you find an algorithm that runs in O(m + n) time?

---

## Espanol

Dadas dos cadenas `s` y `t` de longitudes `m` y `n` respectivamente, devuelve la **subcadena de ventana minima** de `s` tal que cada caracter en `t` (**incluyendo duplicados**) este incluido en la ventana. Si no existe tal subcadena, devuelve la cadena vacia `""`.

Los casos de prueba se generaran de modo que la respuesta sea **unica**.

### Ejemplos

#### Ejemplo 1
```text
Entrada: s = "ADOBECODEBANC", t = "ABC"
Salida: "BANC"
Explicacion: La subcadena de ventana minima "BANC" incluye 'A', 'B' y 'C' de la cadena t.
```

#### Ejemplo 2
```text
Entrada: s = "a", t = "a"
Salida: "a"
Explicacion: La cadena completa s es la ventana minima.
```

#### Ejemplo 3
```text
Entrada: s = "a", t = "aa"
Salida: ""
Explicacion: Ambas 'a' de t deben estar incluidas en la ventana. Como la ventana mas grande de s solo tiene una 'a', se devuelve una cadena vacia.
```

### Restricciones

- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- `s` y `t` consisten en letras mayusculas y minusculas del ingles.

### Desafio adicional

Podrias encontrar un algoritmo que se ejecute en tiempo O(m + n)?
