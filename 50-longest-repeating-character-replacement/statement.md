# 50. Longest Repeating Character Replacement / Reemplazo del Caracter Repetido Mas Largo

## English

You are given a string `s` and an integer `k`. You can choose any character in the string and change it to any other **uppercase English letter**. You may perform this operation **at most `k` times**.

Return the **length of the longest substring** containing the same letter that you can obtain after performing the operations.

### Examples

#### Example 1
```text
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A' characters with 'B' (or vice versa) to get a substring of length 4 with the same letter.
```

#### Example 2
```text
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the 'A' in the middle with 'B' to form "AABBBBA". The substring "BBBB" has length 4, which is the maximum.
```

### Constraints

- `1 <= s.length <= 10^5`
- `s` consists of only uppercase English letters.
- `0 <= k <= s.length`

---

## Espanol

Se te da una cadena `s` y un entero `k`. Puedes elegir cualquier caracter de la cadena y cambiarlo por cualquier **letra mayuscula del alfabeto ingles**. Puedes realizar esta operacion **como maximo `k` veces**.

Devuelve la **longitud de la subcadena mas larga** que contenga la misma letra despues de realizar las operaciones.

### Ejemplos

#### Ejemplo 1
```text
Entrada: s = "ABAB", k = 2
Salida: 4
Explicacion: Reemplaza las dos 'A' por 'B' (o viceversa) para obtener una subcadena de longitud 4 con la misma letra.
```

#### Ejemplo 2
```text
Entrada: s = "AABABBA", k = 1
Salida: 4
Explicacion: Reemplaza la 'A' del medio por 'B' para formar "AABBBBA". La subcadena "BBBB" tiene longitud 4, que es el maximo.
```

### Restricciones

- `1 <= s.length <= 10^5`
- `s` consiste unicamente en letras mayusculas del alfabeto ingles.
- `0 <= k <= s.length`
