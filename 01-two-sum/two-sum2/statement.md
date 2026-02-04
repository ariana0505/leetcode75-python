# 🧩 1. Two Sum II - Input Array Is Sorted / Dos Números que Suman II (Arreglo Ordenado)

## 🇬🇧 English Version

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where:

`1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, as a 1-indexed integer array `[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

### 🧠 Examples

#### Example 1
```text
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.
```

#### Example 2
```text
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3.
```

#### Example 3
```text
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2.
```

### ⚙️ Constraints

- 2 <= `numbers.length` <= 3 * 10^4
- -1000 <= `numbers[i]` <= 1000
- `numbers` is sorted in non-decreasing order
- -1000 <= `target` <= 1000
- There is exactly one valid solution

---

## 🇪🇸 Versión en Español

Dado un arreglo de enteros indexado desde 1 llamado `numbers`, que ya está ordenado de forma no decreciente, encuentra dos números que sumen un valor específico `target`.
Estos dos números serán `numbers[index1]` y `numbers[index2]`, donde:

`1 <= index1 < index2 <= numbers.length`.

Devuelve los índices de estos dos números, `index1` y `index2`, como un arreglo 1-indexado de enteros `[index1, index2]`.

Las pruebas garantizan que existe exactamente una solución. No puedes usar el mismo elemento dos veces.

Tu solución debe usar solo espacio adicional constante.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: numbers = [2,7,11,15], target = 9
Salida: [1,2]
Explicación: La suma de 2 y 7 es 9, por lo tanto index1 = 1, index2 = 2.
```

#### Ejemplo 2
```text
Entrada: numbers = [2,3,4], target = 6
Salida: [1,3]
Explicación: La suma de 2 y 4 es 6, así que index1 = 1, index2 = 3.
```

#### Ejemplo 3
```text
Entrada: numbers = [-1,0], target = -1
Salida: [1,2]
Explicación: La suma de -1 y 0 es -1, por lo tanto index1 = 1, index2 = 2.
```

### ⚙️ Restricciones

- 2 <= `numbers.length` <= 3 * 10^4
- -1000 <= `numbers[i]` <= 1000
- `numbers` está ordenado de forma no decreciente
- -1000 <= `target` <= 1000
- Existe exactamente una solución válida


