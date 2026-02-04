## Product of Array Except Self (English)

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in **O(n)** time and **without using the division operation**.

### Example 1
**Input:** `nums = [1,2,3,4]`  
**Output:** `[24,12,8,6]`

### Example 2
**Input:** `nums = [-1,1,0,-3,3]`  
**Output:** `[0,0,9,0,0]`

### Constraints
- `2 <= nums.length <= 10^5`  
- `-30 <= nums[i] <= 30`  
- The input is generated such that `answer[i]` fits in a 32-bit integer.

### Follow-up
Can you solve the problem in **O(1) extra space** complexity?  
(The output array does not count as extra space.)

---

## Producto del Arreglo Excepto a Sí Mismo (Español)

Dado un arreglo de enteros `nums`, devuelve un arreglo `answer` tal que `answer[i]` es igual al producto de todos los elementos de `nums` excepto `nums[i]`.

Se garantiza que el producto de cualquier prefijo o sufijo de `nums` cabe en un entero de 32 bits.

Debes escribir un algoritmo que funcione en **O(n)** tiempo y **sin usar la operación de división**.

### Ejemplo 1
**Entrada:** `nums = [1,2,3,4]`  
**Salida:** `[24,12,8,6]`

### Ejemplo 2
**Entrada:** `nums = [-1,1,0,-3,3]`  
**Salida:** `[0,0,9,0,0]`

### Restricciones
- `2 <= nums.length <= 10^5`  
- `-30 <= nums[i] <= 30`  
- Se garantiza que `answer[i]` cabe en un entero de 32 bits.

### Follow-up
¿Puedes resolver el problema usando **O(1) espacio extra**?  
(El arreglo de salida no cuenta como espacio extra.)