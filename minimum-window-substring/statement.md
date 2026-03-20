# 🧩 76. Minimum Window Substring / Subcadena de Ventana Mínima

## 🇬🇧 English Version

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (**including duplicates**) is included in the window. If there is no such substring, return the empty string `""`.

The testcases will be generated such that the answer is **unique**.

### 🧠 Examples

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

### ⚙️ Constraints

- m == s.length
- n == t.length
- 1 <= m, n <= 10⁵
- `s` and `t` consist of uppercase and lowercase English letters.

### 🚀 Follow-up

Could you find an algorithm that runs in O(m + n) time?

---

## 🇪🇸 Versión en Español

Dadas dos cadenas `s` y `t` de longitudes `m` y `n` respectivamente, devuelve la **subcadena de ventana mínima** de `s` tal que cada carácter en `t` (**incluyendo duplicados**) esté incluido en la ventana. Si no existe tal subcadena, devuelve la cadena vacía `""`.

Los casos de prueba se generarán de modo que la respuesta sea **única**.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: s = "ADOBECODEBANC", t = "ABC"
Salida: "BANC"
Explicación: La subcadena de ventana mínima "BANC" incluye 'A', 'B' y 'C' de la cadena t.
```

#### Ejemplo 2
```text
Entrada: s = "a", t = "a"
Salida: "a"
Explicación: La cadena completa s es la ventana mínima.
```

#### Ejemplo 3
```text
Entrada: s = "a", t = "aa"
Salida: ""
Explicación: Ambas 'a' de t deben estar incluidas en la ventana. Como la ventana más grande de s solo tiene una 'a', se devuelve una cadena vacía.
```

### ⚙️ Restricciones

- m == s.length
- n == t.length
- 1 <= m, n <= 10⁵
- `s` y `t` consisten en letras mayúsculas y minúsculas del inglés.

### 🚀 Desafío adicional

¿Podrías encontrar un algoritmo que se ejecute en tiempo O(m + n)?
