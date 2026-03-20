# 🧩 141. Linked List Cycle / Ciclo en Lista Enlazada

## 🇬🇧 English Version

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### 🧠 Examples

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

### ⚙️ Constraints

- The number of the nodes in the list is in the range [0, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- `pos` is -1 or a valid index in the linked list.

### 🚀 Follow-up

Can you solve it using O(1) (i.e. constant) memory?

---

## 🇪🇸 Versión en Español

Dado `head`, la cabeza de una lista enlazada, determina si la lista enlazada tiene un ciclo.

Hay un ciclo en una lista enlazada si existe algún nodo en la lista al que se puede llegar de nuevo siguiendo continuamente el puntero `next`. Internamente, `pos` se usa para indicar el índice del nodo al que está conectado el puntero `next` de la cola. **Ten en cuenta que `pos` no se pasa como parámetro.**

Devuelve `true` si hay un ciclo en la lista enlazada. De lo contrario, devuelve `false`.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: head = [3,2,0,-4], pos = 1
Salida: true
Explicación: Hay un ciclo en la lista enlazada, donde la cola se conecta al nodo en la posición 1 (indexado desde 0).
```

#### Ejemplo 2
```text
Entrada: head = [1,2], pos = 0
Salida: true
Explicación: Hay un ciclo en la lista enlazada, donde la cola se conecta al nodo en la posición 0.
```

#### Ejemplo 3
```text
Entrada: head = [1], pos = -1
Salida: false
Explicación: No hay ciclo en la lista enlazada.
```

### ⚙️ Restricciones

- El número de nodos en la lista está en el rango [0, 10⁴].
- -10⁵ <= Node.val <= 10⁵
- `pos` es -1 o un índice válido en la lista enlazada.

### 🚀 Desafío adicional

¿Puedes resolverlo usando O(1) (es decir, constante) de memoria?
