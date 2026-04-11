# 18. Jump Game / Juego de Saltos

## English

You are given an integer array `nums`. You are initially positioned at the array's **first index**, and each element in the array represents your **maximum jump length** at that position.

Return `true` if you can reach the **last index**, or `false` otherwise.

### Examples

#### Example 1
```text
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

#### Example 2
```text
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what.
  Its maximum jump length is 0, which makes it impossible to reach the last index.
```

### Constraints

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`

---

## Espanol

Se te da un arreglo de enteros `nums`. Empiezas en el **primer indice** del arreglo, y cada elemento representa la **longitud maxima de salto** en esa posicion.

Devuelve `true` si puedes llegar al **ultimo indice**, o `false` en caso contrario.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [2,3,1,1,4]
Salida: true
Explicacion: Salta 1 paso del indice 0 al 1, luego 3 pasos al ultimo indice.
```

#### Ejemplo 2
```text
Entrada: nums = [3,2,1,0,4]
Salida: false
Explicacion: Siempre llegaras al indice 3 sin importar que.
  Su longitud maxima de salto es 0, lo que hace imposible llegar al ultimo indice.
```

### Restricciones

- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`
