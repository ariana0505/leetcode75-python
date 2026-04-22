# 67. Kth Smallest Element in a BST / K-esimo Elemento mas Pequeno en un BST

## English

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (**1-indexed**) of all the values of the nodes in the tree.

### Examples

#### Example 1
```text
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

#### Example 2
```text
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

### Constraints

- The number of nodes in the tree is `n`.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

### Follow-up

If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

---

## Espanol

Dada la raiz `root` de un arbol de busqueda binaria y un entero `k`, devuelve el k-esimo valor mas pequeno (**indexado desde 1**) entre todos los valores de los nodos del arbol.

### Ejemplos

#### Ejemplo 1
```text
Entrada: root = [3,1,4,null,2], k = 1
Salida: 1
```

#### Ejemplo 2
```text
Entrada: root = [5,3,6,2,4,null,null,1], k = 3
Salida: 3
```

### Restricciones

- El numero de nodos en el arbol es `n`.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

### Desafio adicional

Si el BST se modifica con frecuencia (es decir, podemos realizar inserciones y eliminaciones) y necesitas encontrar el k-esimo mas pequeno a menudo, como lo optimizarias?
