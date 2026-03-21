# 64. Subtree of Another Tree / Subarbol de Otro Arbol

## English

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### Examples

#### Example 1
```text
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

#### Example 2
```text
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

### Constraints

- The number of nodes in the `root` tree is in the range [1, 2000].
- The number of nodes in the `subRoot` tree is in the range [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4

---

## Espanol

Dadas las raices de dos arboles binarios `root` y `subRoot`, devuelve `true` si existe un subarbol de `root` con la misma estructura y valores de nodos que `subRoot`, y `false` en caso contrario.

Un subarbol de un arbol binario `tree` es un arbol que consiste en un nodo de `tree` y todos los descendientes de ese nodo. El arbol `tree` tambien se puede considerar como un subarbol de si mismo.

### Ejemplos

#### Ejemplo 1
```text
Entrada: root = [3,4,5,1,2], subRoot = [4,1,2]
Salida: true
```

#### Ejemplo 2
```text
Entrada: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Salida: false
```

### Restricciones

- El numero de nodos en el arbol `root` esta en el rango [1, 2000].
- El numero de nodos en el arbol `subRoot` esta en el rango [1, 1000].
- -10^4 <= root.val <= 10^4
- -10^4 <= subRoot.val <= 10^4
