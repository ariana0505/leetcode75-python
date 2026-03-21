# 20. Combination Sum / Suma de Combinaciones

## English

Given an array of **distinct integers** `candidates` and a target integer `target`, return a list of **all unique combinations** of `candidates` where the chosen numbers sum to `target`.

You may return the combinations in **any order**.

- The same number may be chosen from `candidates` an **unlimited number of times**.
- Two combinations are considered **unique** if the frequency of at least one chosen number is different.
- The test cases are generated such that the total number of unique combinations is **less than 150**.

### Examples

#### Example 1
```text
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
  2 + 2 + 3 = 7 (number 2 can be reused)
  7 = 7
  These are the only valid combinations.
```

#### Example 2
```text
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

#### Example 3
```text
Input: candidates = [2], target = 1
Output: []
```

### Constraints

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- All elements of `candidates` are **distinct**
- `1 <= target <= 40`

---

## Espanol

Dado un arreglo de **enteros distintos** `candidates` y un entero objetivo `target`, devuelve una lista de **todas las combinaciones unicas** de `candidates` cuya suma sea igual a `target`.

Puedes devolver las combinaciones en **cualquier orden**.

- Un mismo numero de `candidates` puede usarse **un numero ilimitado de veces**.
- Dos combinaciones son **unicas** si la frecuencia de al menos uno de los numeros elegidos es diferente.
- Los casos de prueba garantizan que el numero total de combinaciones unicas es **menor a 150**.

### Ejemplos

#### Ejemplo 1
```text
Entrada: candidates = [2,3,6,7], target = 7
Salida: [[2,2,3],[7]]
Explicacion:
  2 + 2 + 3 = 7 (el numero 2 puede reutilizarse)
  7 = 7
  Estas son las unicas combinaciones validas.
```

#### Ejemplo 2
```text
Entrada: candidates = [2,3,5], target = 8
Salida: [[2,2,2,2],[2,3,3],[3,5]]
```

#### Ejemplo 3
```text
Entrada: candidates = [2], target = 1
Salida: []
```

### Restricciones

- `1 <= candidates.length <= 30`
- `2 <= candidates[i] <= 40`
- Todos los elementos de `candidates` son **distintos**
- `1 <= target <= 40`
