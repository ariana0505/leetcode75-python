# 33. Number of Connected Components in an Undirected Graph / Numero de Componentes Conexas en un Grafo No Dirigido

## English

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer `n` and an array `edges` where `edges[i] = [ai, bi]` indicates that there is an edge between `ai` and `bi` in the graph.

Return the number of connected components in the graph.

### Examples

#### Example 1
```text
Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
```

#### Example 2
```text
Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
```

### Constraints

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- There are no repeated edges.

---

## Espanol

Tienes un grafo de `n` nodos etiquetados de `0` a `n - 1`. Se te da un entero `n` y un arreglo `edges` donde `edges[i] = [ai, bi]` indica que existe una arista entre `ai` y `bi` en el grafo.

Devuelve el numero de componentes conexas en el grafo.

### Ejemplos

#### Ejemplo 1
```text
Entrada: n = 5, edges = [[0,1],[1,2],[3,4]]
Salida: 2
```

#### Ejemplo 2
```text
Entrada: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Salida: 1
```

### Restricciones

- 1 <= n <= 2000
- 1 <= edges.length <= 5000
- edges[i].length == 2
- 0 <= ai <= bi < n
- ai != bi
- No hay aristas repetidas.
