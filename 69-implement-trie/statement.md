# 69. Implement Trie (Prefix Tree) / Implementar Trie (Arbol de Prefijos)

## English

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the `Trie` class:

- `Trie()` Initializes the trie object.
- `void insert(String word)` Inserts the string `word` into the trie.
- `boolean search(String word)` Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `boolean startsWith(String prefix)` Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

### Examples

#### Example 1
```text
Input:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output:
[null, null, true, false, true, null, true]

Explanation:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
```

### Constraints

- 1 <= word.length, prefix.length <= 2000
- `word` and `prefix` consist only of lowercase English letters.
- At most 3 * 10^4 calls **in total** will be made to `insert`, `search`, and `startsWith`.

---

## Espanol

Un **trie** (se pronuncia "try") o **arbol de prefijos** es una estructura de datos en forma de arbol que se usa para almacenar y recuperar eficientemente claves en un conjunto de cadenas. Existen varias aplicaciones de esta estructura, como el autocompletado y el corrector ortografico.

Implementa la clase `Trie`:

- `Trie()` Inicializa el objeto trie.
- `void insert(String word)` Inserta la cadena `word` en el trie.
- `boolean search(String word)` Devuelve `true` si la cadena `word` esta en el trie (es decir, fue insertada previamente) y `false` en caso contrario.
- `boolean startsWith(String prefix)` Devuelve `true` si existe alguna cadena `word` previamente insertada que tenga a `prefix` como prefijo, y `false` en caso contrario.

### Ejemplos

#### Ejemplo 1
```text
Entrada:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Salida:
[null, null, true, false, true, null, true]

Explicacion:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // devuelve True
trie.search("app");     // devuelve False
trie.startsWith("app"); // devuelve True
trie.insert("app");
trie.search("app");     // devuelve True
```

### Restricciones

- 1 <= word.length, prefix.length <= 2000
- `word` y `prefix` constan solo de letras minusculas del alfabeto ingles.
- Se haran como maximo 3 * 10^4 llamadas **en total** a `insert`, `search` y `startsWith`.
