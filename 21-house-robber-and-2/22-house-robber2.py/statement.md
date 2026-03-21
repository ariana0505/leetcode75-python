# 22. House Robber II / Ladron de Casas II

## English

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses are arranged in a **circle**, meaning the **first house is adjacent to the last one**.

Additionally, adjacent houses have security systems connected, and the police will be alerted if **two adjacent houses** are robbed on the same night.

Given an integer array `nums` representing the amount of money in each house, return the **maximum amount of money** you can rob **without alerting the police**.

### Examples

#### Example 1
```text
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and house 3 (money = 2) because they are adjacent.
```

#### Example 2
```text
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and house 3 (money = 3). Total = 4.
```

#### Example 3
```text
Input: nums = [1,2,3]
Output: 3
```

### Constraints

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

---

## Espanol

Eres un ladron profesional que planea robar casas a lo largo de una calle. Cada casa tiene una cierta cantidad de dinero guardado. Todas las casas estan organizadas en un **circulo**, lo que significa que la **primera casa es vecina de la ultima**.

Ademas, las casas adyacentes tienen sistemas de seguridad conectados, y la policia sera alertada si se roban **dos casas contiguas** la misma noche.

Dado un arreglo de enteros `nums` que representa la cantidad de dinero en cada casa, devuelve la **cantidad maxima de dinero** que puedes robar **sin alertar a la policia**.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [2,3,2]
Salida: 3
Explicacion: No puedes robar la casa 1 (dinero = 2) y la casa 3 (dinero = 2) porque son adyacentes.
```

#### Ejemplo 2
```text
Entrada: nums = [1,2,3,1]
Salida: 4
Explicacion: Roba la casa 1 (dinero = 1) y la casa 3 (dinero = 3). Total = 4.
```

#### Ejemplo 3
```text
Entrada: nums = [1,2,3]
Salida: 3
```

### Restricciones

- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`
