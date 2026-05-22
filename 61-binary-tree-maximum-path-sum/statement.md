# 61. Binary Tree Maximum Path Sum / Suma Maxima de Camino en Arbol Binario

## English

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

### Examples

#### Example 1
```text
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

#### Example 2
```text
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```

### Constraints

- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000

---

## Espanol

Un camino en un arbol binario es una secuencia de nodos donde cada par de nodos adyacentes esta conectado por una arista. Un nodo puede aparecer como maximo una vez en la secuencia. El camino no necesita pasar por la raiz.

La suma de un camino es la suma de los valores de los nodos que lo componen.

Dada la raiz `root` de un arbol binario, devuelve la suma maxima de cualquier camino no vacio.

### Ejemplos

#### Ejemplo 1
```text
Entrada: root = [1,2,3]
Salida: 6
Explicacion: El camino optimo es 2 -> 1 -> 3 con una suma de 2 + 1 + 3 = 6.
```

#### Ejemplo 2
```text
Entrada: root = [-10,9,20,null,null,15,7]
Salida: 42
Explicacion: El camino optimo es 15 -> 20 -> 7 con una suma de 15 + 20 + 7 = 42.
```

### Restricciones

- El numero de nodos del arbol esta en el rango [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
