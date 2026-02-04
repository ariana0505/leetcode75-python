# 🧩 11. Number of 1 Bits / Hamming Weight

## 🇬🇧 English Version

Given a positive integer `n`, write a function that returns the number of **set bits** in its binary representation (also known as the **Hamming weight**).

### 🧠 Examples

#### Example 1
```text
Input: n = 11
Output: 3
Explanation: Binary representation `1011` has three set bits.
```

#### Example 2
```text
Input: n = 128
Output: 1
```

#### Example 3
```text
Input: n = 2147483645
Output: 30
```

### ⚙️ Constraints

- `1 <= n <= 2^31 - 1`

### 🔁 Follow-up
If this function is called many times, consider using a precomputed lookup table for bytes (0..255) to count bits in O(1) per byte.

---

## 🇪🇸 Versión en Español

Dado un entero positivo `n`, escribe una función que devuelva la cantidad de **bits en 1** en su representación binaria (también conocido como el **peso de Hamming**).

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: n = 11
Salida: 3
Explicación: La representación `1011` tiene tres bits en 1.
```

#### Ejemplo 2
```text
Entrada: n = 128
Salida: 1
```

#### Ejemplo 3
```text
Entrada: n = 2147483645
Salida: 30
```

### ⚙️ Restricciones

- `1 <= n <= 2^31 - 1`

### 🔁 Follow-up
Si la función se llama muchas veces, considera usar una tabla de consulta precalculada para bytes (0..255) y contar bits en O(1) por byte.
## Number of 1 Bits / Hamming Weight (English)

Given a positive integer `n`, write a function that returns the number of **set bits** in its binary representation (also known as the **Hamming weight**).

### Example 1
**Input:** `n = 11`  
**Output:** `3`  

**Explanation:**  
The binary representation `1011` contains three set bits.

### Example 2
**Input:** `n = 128`  
**Output:** `1`  

**Explanation:**  
The binary representation `10000000` contains one set bit.

### Example 3
**Input:** `n = 2147483645`  
**Output:** `30`  

**Explanation:**  
The binary representation `1111111111111111111111111111101` contains thirty set bits.

### Constraints
- `1 <= n <= 2^31 - 1`

### Follow-up
If this function is called many times, how would you **optimize** it?

---

## Número de Bits en 1 / Peso de Hamming (Español)

Dado un entero positivo `n`, escribe una función que devuelva la cantidad de **bits en 1** en su representación binaria (también conocido como el **peso de Hamming**).

### Ejemplo 1
**Entrada:** `n = 11`  
**Salida:** `3`  

**Explicación:**  
La representación binaria `1011` contiene tres bits en 1.

### Ejemplo 2
**Entrada:** `n = 128`  
**Salida:** `1`  

**Explicación:**  
La representación binaria `10000000` contiene un solo bit en 1.

### Ejemplo 3
**Entrada:** `n = 2147483645`  
**Salida:** `30`  

**Explicación:**  
La representación binaria `1111111111111111111111111111101` contiene treinta bits en 1.

### Restricciones
- `1 <= n <= 2^31 - 1`

### Follow-up
Si esta función se llama muchas veces, ¿cómo la **optimizarías**?