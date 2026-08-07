# 70. Design Add and Search Words Data Structure / Disenar Estructura de Datos para Agregar y Buscar Palabras

## English

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the `WordDictionary` class:

- `WordDictionary()` Initializes the object.
- `void addWord(word)` Adds `word` to the data structure, it can be matched later.
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word` or `false` otherwise. `word` may contain dots `'.'` where dots can be matched with any letter.

### Examples

#### Example 1
```text
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
```

### Constraints

- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 2 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.

---

## Espanol

Disena una estructura de datos que soporte agregar nuevas palabras y buscar si un string coincide con alguna palabra agregada previamente.

Implementa la clase `WordDictionary`:

- `WordDictionary()` Inicializa el objeto.
- `void addWord(word)` Agrega `word` a la estructura de datos, para poder buscarla despues.
- `bool search(word)` Devuelve `true` si existe algun string en la estructura de datos que coincida con `word`, o `false` en caso contrario. `word` puede contener puntos `'.'` donde cada punto puede coincidir con cualquier letra.

### Ejemplos

#### Ejemplo 1
```text
Entrada:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Salida:
[null,null,null,null,false,true,true,true]

Explicacion:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // devuelve False
wordDictionary.search("bad"); // devuelve True
wordDictionary.search(".ad"); // devuelve True
wordDictionary.search("b.."); // devuelve True
```

### Restricciones

- 1 <= word.length <= 25
- word en addWord consiste en letras minusculas del alfabeto ingles.
- word en search consiste en '.' o letras minusculas del alfabeto ingles.
- Habra como maximo 2 puntos en word para las consultas de search.
- Se haran como maximo 10^4 llamadas a addWord y search.
