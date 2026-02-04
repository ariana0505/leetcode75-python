# 🧩 12. Counting Bits / Conteo de bits

## 🇬🇧 English Version

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of **1's** in the binary representation of `i`.

### 🧠 Examples

#### Example 1
```text
Input: n = 2
Output: [0,1,1]
Explanation:
0 -> 0
1 -> 1
2 -> 10
```

#### Example 2
```text
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 -> 0
1 -> 1
2 -> 10
3 -> 11
4 -> 100
5 -> 101
```

### ⚙️ Constraints

- `0 <= n <= 10^5`

### 🔁 Follow-up
- A straightforward solution runs in **O(n log n)**; try to achieve **O(n)** time and O(n) space.
- You can compute counts in O(1) per number using dynamic programming relations such as `ans[i] = ans[i >> 1] + (i & 1)` or `ans[i] = ans[i & (i - 1)] + 1`.
- Avoid using built-in population-count functions for the challenge.

---

## 🇪🇸 Versión en Español

Dado un entero `n`, devuelve un arreglo `ans` de longitud `n + 1` tal que para cada `i` (`0 <= i <= n`), `ans[i]` es la cantidad de **bits en 1** en la representación binaria de `i`.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: n = 2
Salida: [0,1,1]
Explicación:
0 -> 0
1 -> 1
2 -> 10
```

#### Ejemplo 2
```text
Entrada: n = 5
Salida: [0,1,1,2,1,2]
Explicación:
0 -> 0
1 -> 1
2 -> 10
3 -> 11
4 -> 100
5 -> 101
```

### ⚙️ Restricciones

- `0 <= n <= 10^5`

### 🔁 Follow-up
- Una solución directa es **O(n log n)**; intenta obtener **O(n)** en tiempo y O(n) en espacio.
- Relaciones útiles: `ans[i] = ans[i >> 1] + (i & 1)` o `ans[i] = ans[i & (i - 1)] + 1`.
- Evita utilizar funciones incorporadas de conteo de bits para el reto.

