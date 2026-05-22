# 23. Decode Ways / Formas de Decodificar

## English

A message containing letters from `A-Z` can be encoded into numbers using the following mapping:

```text
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, `"11106"` can be mapped into:

- `"AAJF"` with the grouping `(1 1 10 6)`
- `"KJF"` with the grouping `(11 10 6)`

Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into `'F'` since `"6"` is different from `"06"`.

Given a string `s` containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

### Examples

#### Example 1
```text
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

#### Example 2
```text
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

#### Example 3
```text
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

### Constraints

- 1 <= s.length <= 100
- s contains only digits and may contain leading zero(s).

---

## Espanol

Un mensaje con letras de `A-Z` puede codificarse en numeros usando el siguiente mapeo:

```text
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

Para decodificar un mensaje, todos los digitos deben agruparse y volver a mapearse a letras usando el mapeo inverso (puede haber varias formas). Por ejemplo, `"11106"` puede mapearse a:

- `"AAJF"` con la agrupacion `(1 1 10 6)`
- `"KJF"` con la agrupacion `(11 10 6)`

La agrupacion `(1 11 06)` no es valida porque `"06"` no puede mapearse a `'F'`, ya que `"6"` es distinto de `"06"`.

Dada una cadena `s` que contiene solo digitos, devuelve el numero de formas de decodificarla.

Los casos de prueba se generan de modo que la respuesta cabe en un entero de 32 bits.

### Ejemplos

#### Ejemplo 1
```text
Entrada: s = "12"
Salida: 2
Explicacion: "12" se puede decodificar como "AB" (1 2) o "L" (12).
```

#### Ejemplo 2
```text
Entrada: s = "226"
Salida: 3
Explicacion: "226" se puede decodificar como "BZ" (2 26), "VF" (22 6) o "BBF" (2 2 6).
```

#### Ejemplo 3
```text
Entrada: s = "06"
Salida: 0
Explicacion: "06" no se puede mapear a "F" por el cero a la izquierda ("6" es distinto de "06").
```

### Restricciones

- 1 <= s.length <= 100
- s contiene solo digitos y puede contener ceros a la izquierda.
