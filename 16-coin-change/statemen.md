## Coin Change (English)

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the **fewest number of coins** that you need to make up that amount.  
If the amount of money **cannot be made up** by any combination of the coins, return `-1`.

You may assume that you have an **infinite number of each kind of coin**.

### Example 1
**Input:** `coins = [1,2,5]`, `amount = 11`  
**Output:** `3`  

**Explanation:**  
`11 = 5 + 5 + 1`

### Example 2
**Input:** `coins = [2]`, `amount = 3`  
**Output:** `-1`

### Example 3
**Input:** `coins = [1]`, `amount = 0`  
**Output:** `0`

### Constraints
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

---

## Cambio de Monedas (Español)

Se te da un arreglo de enteros `coins` que representa monedas de diferentes denominaciones y un entero `amount` que representa una cantidad total de dinero.

Devuelve el **menor número de monedas** necesario para alcanzar esa cantidad.  
Si la cantidad **no puede formarse** con ninguna combinación de las monedas, devuelve `-1`.

Puedes asumir que tienes una **cantidad infinita de cada tipo de moneda**.

### Ejemplo 1
**Entrada:** `coins = [1,2,5]`, `amount = 11`  
**Salida:** `3`  

**Explicación:**  
`11 = 5 + 5 + 1`

### Ejemplo 2
**Entrada:** `coins = [2]`, `amount = 3`  
**Salida:** `-1`

### Ejemplo 3
**Entrada:** `coins = [1]`, `amount = 0`  
**Salida:** `0`

### Restricciones
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`