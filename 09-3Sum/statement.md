# 9. 3Sum / Tres Sumas

## English

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Examples

#### Example 1
```text
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: The distinct triplets are [-1,0,1] and [-1,-1,2]. Order does not matter.
```

#### Example 2
```text
Input: nums = [0,1,1]
Output: []
Explanation: No triplet sums to 0.
```

#### Example 3
```text
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums to 0.
```

### Constraints

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

---

## Espanol

Dado un arreglo de enteros `nums`, devuelve todas las tripletas `[nums[i], nums[j], nums[k]]` tales que `i != j`, `i != k` y `j != k`, y `nums[i] + nums[j] + nums[k] == 0`.

Ten en cuenta que el conjunto de soluciones no debe contener tripletas duplicadas.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [-1,0,1,2,-1,-4]
Salida: [[-1,-1,2],[-1,0,1]]
Explicacion: Las tripletas distintas son [-1,0,1] y [-1,-1,2]. El orden no importa.
```

#### Ejemplo 2
```text
Entrada: nums = [0,1,1]
Salida: []
Explicacion: No existe ninguna tripleta que sume 0.
```

#### Ejemplo 3
```text
Entrada: nums = [0,0,0]
Salida: [[0,0,0]]
Explicacion: La unica tripleta posible suma 0.
```

### Restricciones

- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5
