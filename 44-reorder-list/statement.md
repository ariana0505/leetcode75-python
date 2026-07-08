# 44. Reorder List / Reordenar Lista

## English

You are given the head of a singly linked-list. The list can be represented as:

```text
L0 -> L1 -> ... -> Ln-1 -> Ln
```

Reorder the list to be in the following form:

```text
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
```

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

### Examples

#### Example 1
```text
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

#### Example 2
```text
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

### Constraints

- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

---

## Espanol

Se te da la cabeza de una lista enlazada simple. La lista se puede representar como:

```text
L0 -> L1 -> ... -> Ln-1 -> Ln
```

Reordena la lista para que quede de la siguiente forma:

```text
L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
```

No puedes modificar los valores de los nodos de la lista. Solo se pueden cambiar los nodos en si.

### Ejemplos

#### Ejemplo 1
```text
Entrada: head = [1,2,3,4]
Salida: [1,4,2,3]
```

#### Ejemplo 2
```text
Entrada: head = [1,2,3,4,5]
Salida: [1,5,2,4,3]
```

### Restricciones

- El numero de nodos de la lista esta en el rango [1, 5 * 10^4].
- 1 <= Node.val <= 1000
