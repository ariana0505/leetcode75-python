# 32. Graph Valid Tree / Arbol Valido en un Grafo

## English

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and a list of `edges` where `edges[i] = [ai, bi]` indicates that there is an undirected edge between nodes `ai` and `bi` in the graph.

Return `true` if the edges of the given graph make up a valid tree, and `false` otherwise.

### Examples

#### Example 1
```text
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
```

#### Example 2
```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
```

### Constraints

- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- There are no self-loops or repeated edges.

---

## Espanol

Tienes un grafo de `n` nodos etiquetados de `0` a `n - 1`. Se te da un entero `n` y una lista de `edges` donde `edges[i] = [ai, bi]` indica que existe una arista no dirigida entre los nodos `ai` y `bi` en el grafo.

Devuelve `true` si las aristas del grafo dado forman un arbol valido, y `false` en caso contrario.

### Ejemplos

#### Ejemplo 1
```text
Entrada: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Salida: true
```

#### Ejemplo 2
```text
Entrada: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Salida: false
```

### Restricciones

- 1 <= n <= 2000
- 0 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai, bi < n
- ai != bi
- No hay bucles propios ni aristas repetidas.
