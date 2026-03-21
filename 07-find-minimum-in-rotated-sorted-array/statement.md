# 6. Find Minimum in Rotated Sorted Array / Encontrar el Minimo en un Arreglo Ordenado y Rotado

## English

Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.
For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated 4 times.
- `[0,1,2,4,5,6,7]` if it was rotated 7 times.

Notice that rotating an array `[a[0], a[1], ..., a[n-1]]` one time results in `[a[n-1], a[0], a[1], ..., a[n-2]]`.

Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

### Examples

#### Example 1
```text
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

#### Example 2
```text
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

#### Example 3
```text
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

### Constraints

- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All integers in nums are unique.
- nums is sorted and rotated between 1 and n times.

---

## Espanol

Supon que un arreglo de longitud `n` ordenado en orden ascendente se rota entre `1` y `n` veces.
Por ejemplo, el arreglo `nums = [0,1,2,4,5,6,7]` podria convertirse en:

- `[4,5,6,7,0,1,2]` si se roto 4 veces.
- `[0,1,2,4,5,6,7]` si se roto 7 veces.

Ten en cuenta que rotar un arreglo `[a[0], a[1], ..., a[n-1]]` una vez da como resultado `[a[n-1], a[0], a[1], ..., a[n-2]]`.

Dado el arreglo ordenado y rotado `nums` con elementos unicos, devuelve el elemento minimo del arreglo.

Debes escribir un algoritmo que funcione en O(log n) tiempo.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [3,4,5,1,2]
Salida: 1
Explicacion: El arreglo original era [1,2,3,4,5] rotado 3 veces.
```

#### Ejemplo 2
```text
Entrada: nums = [4,5,6,7,0,1,2]
Salida: 0
Explicacion: El arreglo original era [0,1,2,4,5,6,7] y fue rotado 4 veces.
```

#### Ejemplo 3
```text
Entrada: nums = [11,13,15,17]
Salida: 11
Explicacion: El arreglo original era [11,13,15,17] y fue rotado 4 veces.
```

### Restricciones

- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- Todos los numeros en nums son unicos.
- nums esta ordenado y rotado entre 1 y n veces.
