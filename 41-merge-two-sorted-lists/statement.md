# 41. Merge Two Sorted Lists / Unir Dos Listas Enlazadas Ordenadas

## English

You are given the heads of two **sorted linked lists** `list1` and `list2`.

Merge the two lists into **one sorted list**. The new list should be made by **splicing together the nodes** of the first two lists.

Return the **head of the merged linked list**.

### Examples

#### Example 1
```text
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

#### Example 2
```text
Input: list1 = [], list2 = []
Output: []
```

#### Example 3
```text
Input: list1 = [], list2 = [0]
Output: [0]
```

### Constraints

- The number of nodes in both lists is in the range `[0, 50]`
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing order**

---

## Espanol

Se te dan las cabezas de dos **listas enlazadas ordenadas** `list1` y `list2`.

Fusiona ambas listas en **una sola lista ordenada**. La nueva lista debe construirse **uniendo los nodos** de las dos listas originales.

Devuelve la **cabeza de la lista enlazada resultante**.

### Ejemplos

#### Ejemplo 1
```text
Entrada: list1 = [1,2,4], list2 = [1,3,4]
Salida: [1,1,2,3,4,4]
```

#### Ejemplo 2
```text
Entrada: list1 = [], list2 = []
Salida: []
```

#### Ejemplo 3
```text
Entrada: list1 = [], list2 = [0]
Salida: [0]
```

### Restricciones

- El numero de nodos en ambas listas esta en el rango `[0, 50]`
- `-100 <= Node.val <= 100`
- Tanto `list1` como `list2` estan ordenadas en **orden no decreciente**
