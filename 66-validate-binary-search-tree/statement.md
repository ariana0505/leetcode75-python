# 66. Validate Binary Search Tree / Validar Arbol de Busqueda Binaria

## English

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

### Examples

#### Example 1
```text
Input: root = [2,1,3]
Output: true
```

#### Example 2
```text
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

### Constraints

- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1

---

## Espanol

Dada la raiz `root` de un arbol binario, determina si es un arbol de busqueda binaria (BST) valido.

Un **BST valido** se define de la siguiente manera:
- El subarbol izquierdo de un nodo contiene solo nodos con claves **menores que** la clave del nodo.
- El subarbol derecho de un nodo contiene solo nodos con claves **mayores que** la clave del nodo.
- Tanto el subarbol izquierdo como el derecho tambien deben ser arboles de busqueda binaria.

### Ejemplos

#### Ejemplo 1
```text
Entrada: root = [2,1,3]
Salida: true
```

#### Ejemplo 2
```text
Entrada: root = [5,1,4,null,null,3,6]
Salida: false
Explicacion: El valor del nodo raiz es 5, pero el valor de su hijo derecho es 4.
```

### Restricciones

- El numero de nodos en el arbol esta en el rango [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
