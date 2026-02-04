# 🧩 8. Search in Rotated Sorted Array / Buscar en un Arreglo Ordenado Rotado

## 🇬🇧 English Version

Given an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown index `k` (1 <= k < nums.length) such that the resulting array becomes:

`[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed).

For example, `[0,1,2,4,5,6,7]` might be rotated by 3 positions and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not.

You must write an algorithm with `O(log n)` runtime complexity.

### 🧠 Examples

#### Example 1
```text
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

#### Example 2
```text
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

#### Example 3
```text
Input: nums = [1], target = 0
Output: -1
```

### ⚙️ Constraints

- 1 <= `nums.length` <= 5000
- -10^4 <= `nums[i]` <= 10^4
- All values of `nums` are unique
- `nums` is an ascending array that is possibly rotated
- -10^4 <= `target` <= 10^4

---

## 🇪🇸 Versión en Español

Existe un arreglo de enteros `nums` ordenado en forma ascendente (con valores distintos).

Antes de ser pasado a tu función, `nums` pudo haber sido rotado en un índice desconocido `k` (1 <= k < nums.length) de manera que quede:

`[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (indexado desde 0).

Por ejemplo, `[0,1,2,4,5,6,7]` puede rotarse 3 posiciones y convertirse en `[4,5,6,7,0,1,2]`.

Dado el arreglo `nums` después de la posible rotación y un entero `target`, devuelve el índice de `target` si está en `nums`, o `-1` si no se encuentra.

Debes escribir un algoritmo con complejidad `O(log n)`.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [4,5,6,7,0,1,2], target = 0
Salida: 4
```

#### Ejemplo 2
```text
Entrada: nums = [4,5,6,7,0,1,2], target = 3
Salida: -1
```

#### Ejemplo 3
```text
Entrada: nums = [1], target = 0
Salida: -1
```

### ⚙️ Restricciones

- 1 <= `nums.length` <= 5000
- -10^4 <= `nums[i]` <= 10^4
- Todos los valores de `nums` son únicos
- `nums` es un arreglo ascendente que pudo haber sido rotado
- -10^4 <= `target` <= 10^4