# 17. Longest Increasing Subsequence / Subsecuencia Creciente Mas Larga

## English

Given an integer array `nums`, return the **length of the longest strictly increasing subsequence**.

A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

### Examples

#### Example 1
```text
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], so the length is 4.
```

#### Example 2
```text
Input: nums = [0,1,0,3,2,3]
Output: 4
```

#### Example 3
```text
Input: nums = [7,7,7,7,7,7,7]
Output: 1
```

### Constraints

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

### Follow-up

Can you come up with an algorithm that runs in **O(n log n)** time complexity?

---

## Espanol

Dado un arreglo de enteros `nums`, devuelve la **longitud de la subsecuencia estrictamente creciente mas larga**.

Una subsecuencia es una secuencia que puede obtenerse del arreglo eliminando algunos o ningun elemento, sin cambiar el orden de los elementos restantes.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [10,9,2,5,3,7,101,18]
Salida: 4
Explicacion: La subsecuencia creciente mas larga es [2,3,7,101], por lo tanto su longitud es 4.
```

#### Ejemplo 2
```text
Entrada: nums = [0,1,0,3,2,3]
Salida: 4
```

#### Ejemplo 3
```text
Entrada: nums = [7,7,7,7,7,7,7]
Salida: 1
```

### Restricciones

- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

### Desafio adicional

Puedes proponer un algoritmo que funcione en **O(n log n)** de complejidad temporal?
