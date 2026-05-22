# 54. Valid Palindrome / Palindromo Valido

## English

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples

#### Example 1
```text
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

#### Example 2
```text
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

#### Example 3
```text
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

### Constraints

- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.

---

## Espanol

Una frase es un palindromo si, despues de convertir todas las letras mayusculas en minusculas y eliminar todos los caracteres no alfanumericos, se lee igual de izquierda a derecha que de derecha a izquierda. Los caracteres alfanumericos incluyen letras y numeros.

Dada una cadena `s`, devuelve `true` si es un palindromo, o `false` en caso contrario.

### Ejemplos

#### Ejemplo 1
```text
Entrada: s = "A man, a plan, a canal: Panama"
Salida: true
Explicacion: "amanaplanacanalpanama" es un palindromo.
```

#### Ejemplo 2
```text
Entrada: s = "race a car"
Salida: false
Explicacion: "raceacar" no es un palindromo.
```

#### Ejemplo 3
```text
Entrada: s = " "
Salida: true
Explicacion: s es una cadena vacia "" tras eliminar los caracteres no alfanumericos.
Como una cadena vacia se lee igual en ambos sentidos, es un palindromo.
```

### Restricciones

- 1 <= s.length <= 2 * 10^5
- s contiene unicamente caracteres ASCII imprimibles.
