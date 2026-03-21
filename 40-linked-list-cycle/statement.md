# 40. Linked List Cycle / Ciclo en Lista Enlazada

## English

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Examples

#### Example 1
```text
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

#### Example 2
```text
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

#### Example 3
```text
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

### Constraints

- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- `pos` is -1 or a valid index in the linked list.

### Follow-up

Can you solve it using O(1) (i.e. constant) memory?

---

## Espanol

Dado `head`, la cabeza de una lista enlazada, determina si la lista enlazada tiene un ciclo.

Hay un ciclo en una lista enlazada si existe algun nodo en la lista al que se puede llegar de nuevo siguiendo continuamente el puntero `next`. Internamente, `pos` se usa para indicar el indice del nodo al que esta conectado el puntero `next` de la cola. **Ten en cuenta que `pos` no se pasa como parametro.**

Devuelve `true` si hay un ciclo en la lista enlazada. De lo contrario, devuelve `false`.

### Ejemplos

#### Ejemplo 1
```text
Entrada: head = [3,2,0,-4], pos = 1
Salida: true
Explicacion: Hay un ciclo en la lista enlazada, donde la cola se conecta al nodo en la posicion 1 (indexado desde 0).
```

#### Ejemplo 2
```text
Entrada: head = [1,2], pos = 0
Salida: true
Explicacion: Hay un ciclo en la lista enlazada, donde la cola se conecta al nodo en la posicion 0.
```

#### Ejemplo 3
```text
Entrada: head = [1], pos = -1
Salida: false
Explicacion: No hay ciclo en la lista enlazada.
```

### Restricciones

- El numero de nodos en la lista esta en el rango [0, 10^4].
- -10^5 <= Node.val <= 10^5
- `pos` es -1 o un indice valido en la lista enlazada.

### Desafio adicional

Puedes resolverlo usando O(1) (es decir, constante) de memoria?
