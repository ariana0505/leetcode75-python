# 31. Alien Dictionary / Diccionario Alienigena

## English

There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings `words` from the alien language's dictionary, where the strings in `words` are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no solution, return an empty string `""`. If there are multiple solutions, return any of them.

### Examples

#### Example 1
```text
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
```

#### Example 2
```text
Input: words = ["z","x"]
Output: "zx"
```

#### Example 3
```text
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".
```

### Constraints

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of only lowercase English letters.

---

## Espanol

Existe un nuevo idioma alienigena que usa el alfabeto ingles. Sin embargo, el orden entre las letras es desconocido para ti.

Se te da una lista de strings `words` del diccionario del idioma alienigena, donde los strings en `words` estan ordenados lexicograficamente segun las reglas de este nuevo idioma.

Devuelve un string con las letras unicas del nuevo idioma alienigena ordenadas de forma lexicografica creciente segun las reglas del nuevo idioma. Si no hay solucion, devuelve un string vacio `""`. Si hay multiples soluciones, devuelve cualquiera de ellas.

### Ejemplos

#### Ejemplo 1
```text
Entrada: words = ["wrt","wrf","er","ett","rftt"]
Salida: "wertf"
```

#### Ejemplo 2
```text
Entrada: words = ["z","x"]
Salida: "zx"
```

#### Ejemplo 3
```text
Entrada: words = ["z","x","z"]
Salida: ""
Explicacion: El orden es invalido, entonces se devuelve "".
```

### Restricciones

- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consiste solo de letras minusculas del alfabeto ingles.
