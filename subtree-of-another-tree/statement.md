# 🧩 572. Subtree of Another Tree / Subárbol de Otro Árbol

## 🇬🇧 English Version

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a binary tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a subtree of itself.

### 🧠 Examples

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

### ⚙️ Constraints

- The number of nodes in the `root` tree is in the range [1, 2000].
- The number of nodes in the `subRoot` tree is in the range [1, 1000].
- -10⁴ <= root.val <= 10⁴
- -10⁴ <= subRoot.val <= 10⁴

---

## 🇪🇸 Versión en Español

Dadas las raíces de dos árboles binarios `root` y `subRoot`, devuelve `true` si existe un subárbol de `root` con la misma estructura y valores de nodos que `subRoot`, y `false` en caso contrario.

Un subárbol de un árbol binario `tree` es un árbol que consiste en un nodo de `tree` y todos los descendientes de ese nodo. El árbol `tree` también se puede considerar como un subárbol de sí mismo.

### 🧠 Ejemplos

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

### ⚙️ Restricciones

- El número de nodos en el árbol `root` está en el rango [1, 2000].
- El número de nodos en el árbol `subRoot` está en el rango [1, 1000].
- -10⁴ <= root.val <= 10⁴
- -10⁴ <= subRoot.val <= 10⁴
