# 42. Merge k Sorted Lists / Fusionar k Listas Ordenadas

## English

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

### Examples

#### Example 1
```text
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
```

#### Example 2
```text
Input: lists = []
Output: []
```

#### Example 3
```text
Input: lists = [[]]
Output: []
```

### Constraints

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.

---

## Espanol

Se te da un arreglo de `k` listas enlazadas `lists`, cada lista enlazada esta ordenada en orden ascendente.

Fusiona todas las listas enlazadas en una sola lista enlazada ordenada y devuelvela.

### Ejemplos

#### Ejemplo 1
```text
Entrada: lists = [[1,4,5],[1,3,4],[2,6]]
Salida: [1,1,2,3,4,4,5,6]
Explicacion: Las listas enlazadas son:
[
  1->4->5,
  1->3->4,
  2->6
]
al fusionarlas en una sola lista ordenada:
1->1->2->3->4->4->5->6
```

#### Ejemplo 2
```text
Entrada: lists = []
Salida: []
```

#### Ejemplo 3
```text
Entrada: lists = [[]]
Salida: []
```

### Restricciones

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] esta ordenada en orden ascendente.
- La suma de lists[i].length no excedera 10^4.
