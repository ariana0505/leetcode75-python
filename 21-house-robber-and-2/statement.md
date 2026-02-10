## House Robber (English)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, but there is one important constraint: **adjacent houses have security systems connected**, and if two adjacent houses are robbed on the same night, the police will be alerted.

Given an integer array `nums` representing the amount of money in each house, return the **maximum amount of money** you can rob **without alerting the police**.

### Example 1
**Input:** `nums = [1,2,3,1]`  
**Output:** `4`  

**Explanation:**  
Rob house 1 (money = `1`) and house 3 (money = `3`).  
Total = `1 + 3 = 4`.

### Example 2
**Input:** `nums = [2,7,9,3,1]`  
**Output:** `12`  

**Explanation:**  
Rob house 1 (money = `2`), house 3 (money = `9`), and house 5 (money = `1`).  
Total = `2 + 9 + 1 = 12`.

### Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`

---

## Ladrón de Casas (Español)

Eres un ladrón profesional que planea robar casas a lo largo de una calle. Cada casa tiene una cierta cantidad de dinero guardado, pero existe una restricción importante: **las casas adyacentes tienen sistemas de seguridad conectados**, y si se roban dos casas contiguas la misma noche, la policía será alertada.

Dado un arreglo de enteros `nums` que representa la cantidad de dinero en cada casa, devuelve la **cantidad máxima de dinero** que puedes robar **sin alertar a la policía**.

### Ejemplo 1
**Entrada:** `nums = [1,2,3,1]`  
**Salida:** `4`  

**Explicación:**  
Roba la casa 1 (dinero = `1`) y la casa 3 (dinero = `3`).  
Total = `1 + 3 = 4`.

### Ejemplo 2
**Entrada:** `nums = [2,7,9,3,1]`  
**Salida:** `12`  

**Explicación:**  
Roba la casa 1 (dinero = `2`), la casa 3 (dinero = `9`) y la casa 5 (dinero = `1`).  
Total = `2 + 9 + 1 = 12`.

### Restricciones
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`
