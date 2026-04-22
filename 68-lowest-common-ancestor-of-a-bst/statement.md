# 68. Lowest Common Ancestor of a Binary Search Tree / Ancestro Comun mas Bajo de un Arbol de Busqueda Binaria

## English

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**)."

### Examples

#### Example 1
```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
```

#### Example 2
```text
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
```

#### Example 3
```text
Input: root = [2,1], p = 2, q = 1
Output: 2
```

### Constraints

- The number of nodes in the tree is in the range [2, 10^5].
- -10^9 <= Node.val <= 10^9
- All `Node.val` are **unique**.
- `p != q`
- `p` and `q` will exist in the BST.

---

## Espanol

Dado un arbol de busqueda binaria (BST), encuentra el nodo ancestro comun mas bajo (LCA) de dos nodos dados en el BST.

Segun la definicion de LCA en Wikipedia: "El ancestro comun mas bajo se define entre dos nodos `p` y `q` como el nodo mas bajo en `T` que tiene tanto a `p` como a `q` como descendientes (donde permitimos que **un nodo sea descendiente de si mismo**)."

### Ejemplos

#### Ejemplo 1
```text
Entrada: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Salida: 6
Explicacion: El LCA de los nodos 2 y 8 es 6.
```

#### Ejemplo 2
```text
Entrada: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Salida: 2
Explicacion: El LCA de los nodos 2 y 4 es 2, ya que un nodo puede ser descendiente de si mismo segun la definicion de LCA.
```

#### Ejemplo 3
```text
Entrada: root = [2,1], p = 2, q = 1
Salida: 2
```

### Restricciones

- El numero de nodos en el arbol esta en el rango [2, 10^5].
- -10^9 <= Node.val <= 10^9
- Todos los `Node.val` son **unicos**.
- `p != q`
- `p` y `q` existiran en el BST.
