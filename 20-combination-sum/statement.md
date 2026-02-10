## Combination Sum (English)

Given an array of **distinct integers** `candidates` and a target integer `target`, return a list of **all unique combinations** of `candidates` where the chosen numbers sum to `target`.

You may return the combinations in **any order**.

- The same number may be chosen from `candidates` an **unlimited number of times**.
- Two combinations are considered **unique** if the frequency of at least one chosen number is different.
- The test cases are generated such that the total number of unique combinations is **less than 150**.

### Example 1
**Input:** `candidates = [2,3,6,7]`, `target = 7`  
**Output:** `[[2,2,3],[7]]`

**Explanation:**  
- `2 + 2 + 3 = 7` (number `2` can be reused)  
- `7 = 7`  
These are the only valid combinations.

### Example 2
**Input:** `candidates = [2,3,5]`, `target = 8`  
**Output:** `[[2,2,2,2],[2,3,3],[3,5]]`

### Example 3
**Input:** `candidates = [2]`, `target = 1`  
**Output:** `[]`

### Constraints
- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**
- `1 <= target <= 40`

---

## Suma de Combinaciones (Español)

Dado un arreglo de **enteros distintos** `candidates` y un entero objetivo `target`, devuelve una lista de **todas las combinaciones únicas** de `candidates` cuya suma sea igual a `target`.

Puedes devolver las combinaciones en **cualquier orden**.

- Un mismo número de `candidates` puede usarse **un número ilimitado de veces**.
- Dos combinaciones son **únicas** si la frecuencia de al menos uno de los números elegidos es diferente.
- Los casos de prueba garantizan que el número total de combinaciones únicas es **menor a 150**.

### Ejemplo 1
**Entrada:** `candidates = [2,3,6,7]`, `target = 7`  
**Salida:** `[[2,2,3],[7]]`

**Explicación:**  
- `2 + 2 + 3 = 7` (el nú
