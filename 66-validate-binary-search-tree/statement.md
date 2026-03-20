# 🧩 98. Validate Binary Search Tree / Validar Árbol de Búsqueda Binaria

## 🇬🇧 English Version

Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).

A **valid BST** is defined as follows:
- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

### 🧠 Examples

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

### ⚙️ Constraints

- The number of nodes in the tree is in the range [1, 10⁴].
- -2³¹ <= Node.val <= 2³¹ - 1

---

## 🇪🇸 Versión en Español

Dada la raíz `root` de un árbol binario, determina si es un árbol de búsqueda binaria (BST) válido.

Un **BST válido** se define de la siguiente manera:
- El subárbol izquierdo de un nodo contiene solo nodos con claves **menores que** la clave del nodo.
- El subárbol derecho de un nodo contiene solo nodos con claves **mayores que** la clave del nodo.
- Tanto el subárbol izquierdo como el derecho también deben ser árboles de búsqueda binaria.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: root = [2,1,3]
Salida: true
```

#### Ejemplo 2
```text
Entrada: root = [5,1,4,null,null,3,6]
Salida: false
Explicación: El valor del nodo raíz es 5, pero el valor de su hijo derecho es 4.
```

### ⚙️ Restricciones

- El número de nodos en el árbol está en el rango [1, 10⁴].
- -2³¹ <= Node.val <= 2³¹ - 1
