# 6. Maximum Product Subarray / Maximo Producto de un Subarray

## English

Given an integer array `nums`, find a (contiguous) subarray that has the largest product, and return that product (an integer).

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is simply the value of that element.

### Examples

#### Example 1
```text
Input: nums = [2, 3, -2, 4]
Output: 6
Explanation: The subarray [2, 3] has the largest product: 2 * 3 = 6.
```

#### Example 2
```text
Input: nums = [-2, 0, -1]
Output: 0
Explanation: The subarray with the maximum product is [0], whose product is 0.
```

### Constraints

- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

---

## Espanol

Dado un arreglo de enteros `nums`, encuentra un subarray (contiguo) que tenga el producto mas grande y devuelve dicho producto (un entero).

Los casos de prueba estan generados de tal forma que la respuesta siempre encajara en un entero de 32 bits.

Ten en cuenta que el producto de un arreglo con un solo elemento es simplemente el valor de ese elemento.

### Ejemplos

#### Ejemplo 1
```text
Entrada: nums = [2, 3, -2, 4]
Salida: 6
Explicacion: El subarray [2, 3] tiene el producto maximo: 2 * 3 = 6.
```

#### Ejemplo 2
```text
Entrada: nums = [-2, 0, -1]
Salida: 0
Explicacion: El subarray con producto maximo es [0], cuyo producto es 0.
```

### Restricciones

- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- El producto de cualquier subarray de nums esta garantizado que cabe en un entero de 32 bits.
