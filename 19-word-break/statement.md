# 19. Word Break / Separacion de Palabras

## English

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a **space-separated sequence of one or more dictionary words**.

Note that the same word in the dictionary **may be reused multiple times** in the segmentation.

### Examples

#### Example 1
```text
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

#### Example 2
```text
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple". The word "apple" is reused.
```

#### Example 3
```text
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

### Constraints

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters.
- All the strings of `wordDict` are **unique**.

---

## Espanol

Dada una cadena `s` y un diccionario de cadenas `wordDict`, devuelve `true` si `s` puede segmentarse en una **secuencia de una o mas palabras del diccionario separadas por espacios**.

Ten en cuenta que la misma palabra del diccionario **puede reutilizarse multiples veces** en la segmentacion.

### Ejemplos

#### Ejemplo 1
```text
Entrada: s = "leetcode", wordDict = ["leet","code"]
Salida: true
Explicacion: Devuelve true porque "leetcode" puede segmentarse como "leet code".
```

#### Ejemplo 2
```text
Entrada: s = "applepenapple", wordDict = ["apple","pen"]
Salida: true
Explicacion: Devuelve true porque "applepenapple" puede segmentarse como "apple pen apple". La palabra "apple" se reutiliza.
```

#### Ejemplo 3
```text
Entrada: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Salida: false
```

### Restricciones

- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` y `wordDict[i]` consisten solo de letras minusculas del alfabeto ingles.
- Todas las cadenas de `wordDict` son **unicas**.
