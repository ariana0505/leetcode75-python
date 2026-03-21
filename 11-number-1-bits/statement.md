# 11. Number of 1 Bits / Numero de Bits en 1

## English

Given a positive integer `n`, write a function that returns the number of **set bits** in its binary representation (also known as the **Hamming weight**).

### Examples

#### Example 1
```text
Input: n = 11
Output: 3
Explanation: Binary representation 1011 has three set bits.
```

#### Example 2
```text
Input: n = 128
Output: 1
Explanation: Binary representation 10000000 has one set bit.
```

#### Example 3
```text
Input: n = 2147483645
Output: 30
Explanation: Binary representation 1111111111111111111111111111101 has thirty set bits.
```

### Constraints

- `1 <= n <= 2^31 - 1`

### Follow-up

If this function is called many times, how would you optimize it? Consider using a precomputed lookup table for bytes (0..255) to count bits in O(1) per byte.

---

## Espanol

Dado un entero positivo `n`, escribe una funcion que devuelva la cantidad de **bits en 1** en su representacion binaria (tambien conocido como el **peso de Hamming**).

### Ejemplos

#### Ejemplo 1
```text
Entrada: n = 11
Salida: 3
Explicacion: La representacion binaria 1011 contiene tres bits en 1.
```

#### Ejemplo 2
```text
Entrada: n = 128
Salida: 1
Explicacion: La representacion binaria 10000000 contiene un solo bit en 1.
```

#### Ejemplo 3
```text
Entrada: n = 2147483645
Salida: 30
Explicacion: La representacion binaria 1111111111111111111111111111101 contiene treinta bits en 1.
```

### Restricciones

- `1 <= n <= 2^31 - 1`

### Desafio adicional

Si esta funcion se llama muchas veces, como la optimizarias? Considera usar una tabla de consulta precalculada para bytes (0..255) y contar bits en O(1) por byte.
