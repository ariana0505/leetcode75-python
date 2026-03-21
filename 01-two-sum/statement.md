# 1. Two Sum / Dos Numeros que Suman

## English

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples

#### Example 1
```text
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

#### Example 2
```text
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

#### Example 3
```text
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

### Follow-up

Can you come up with an algorithm that has less than O(n^2) time complexity?

---

## Espanol

Dado un arreglo de enteros `nums` y un entero `target`, devuelve los indices de los dos numeros tales que su suma sea igual a `target`.

Puedes asumir que cada entrada tiene exactamente una solucion, y que no puedes usar el mismo elemento dos veces.

Puedes devolver la respuesta en cualquier orden.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [2,7,11,15], target = 9
Salida: [0,1]
Explicacion: Como nums[0] + nums[1] == 9, devolvemos [0, 1].
```

#### Ejemplo 2
```text
Entrada: nums = [3,2,4], target = 6
Salida: [1,2]
```

#### Ejemplo 3
```text
Entrada: nums = [3,3], target = 6
Salida: [0,1]
```

### Restricciones

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Solo existe una respuesta valida.

### Desafio adicional

Puedes crear un algoritmo cuya complejidad sea menor que O(n^2)?
