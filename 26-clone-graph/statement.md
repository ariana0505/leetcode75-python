# 26. Clone Graph / Clonar Grafo

## English

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```text
class Node {
    public int val;
    public List<Node> neighbors;
}
```

The graph is represented in the test case using an adjacency list. An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with `val = 1`. You must return the copy of the given node as a reference to the cloned graph.

### Examples

#### Example 1
```text
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
```

#### Example 2
```text
Input: adjList = [[]]
Output: [[]]
Explanation: The graph has one node with no neighbors.
```

#### Example 3
```text
Input: adjList = []
Output: []
Explanation: The graph is empty.
```

### Constraints

- The number of nodes in the graph is in the range [0, 100].
- 1 <= Node.val <= 100
- Node.val is unique for each node.
- There are no repeated edges and no self-loops in the graph.
- The Graph is connected and all nodes can be visited starting from the given node.

---

## Espanol

Dada una referencia de un nodo en un grafo no dirigido y conexo, devuelve una copia profunda (clon) del grafo.

Cada nodo del grafo contiene un valor (`int`) y una lista (`List[Node]`) de sus vecinos.

```text
class Node {
    public int val;
    public List<Node> neighbors;
}
```

El grafo se representa en el caso de prueba usando una lista de adyacencia. Una lista de adyacencia es una coleccion de listas desordenadas que se usa para representar un grafo finito. Cada lista describe el conjunto de vecinos de un nodo del grafo.

El nodo dado siempre sera el primer nodo con `val = 1`. Debes devolver la copia del nodo dado como referencia al grafo clonado.

### Ejemplos

#### Ejemplo 1
```text
Entrada: adjList = [[2,4],[1,3],[2,4],[1,3]]
Salida: [[2,4],[1,3],[2,4],[1,3]]
Explicacion: Hay 4 nodos en el grafo.
```

#### Ejemplo 2
```text
Entrada: adjList = [[]]
Salida: [[]]
Explicacion: El grafo tiene un nodo sin vecinos.
```

#### Ejemplo 3
```text
Entrada: adjList = []
Salida: []
Explicacion: El grafo esta vacio.
```

### Restricciones

- El numero de nodos del grafo esta en el rango [0, 100].
- 1 <= Node.val <= 100
- Node.val es unico para cada nodo.
- No hay aristas repetidas ni bucles propios en el grafo.
- El grafo es conexo y todos los nodos pueden visitarse partiendo del nodo dado.
