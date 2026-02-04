# 🧩 3. Best Time to Buy and Sell Stock / Mejor Momento para Comprar y Vender Acciones

## 🇬🇧 English Version

You are given an array `prices` where `prices[i]` is the price of a given stock on the *i-th* day.

You want to **maximize your profit** by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the **maximum profit** you can achieve from this transaction.  
If you cannot achieve any profit, return `0`.

### 🧠 Examples

#### Example 1
```text
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

#### Example 2
```text
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### ⚙️ Constraints

- 1 <= prices.length <= 10⁵
- 0 <= prices[i] <= 10⁴

---

## 🇪🇸 Versión en Español

Se te da un arreglo `prices` donde `prices[i]` es el precio de una acción en el día *i*.

Deseas **maximizar tu ganancia** eligiendo un día para comprar una acción y un día diferente en el futuro para venderla.

Devuelve la **máxima ganancia** que puedes obtener de esta transacción.  
Si no puedes obtener ninguna ganancia, devuelve `0`.

### 🧠 Ejemplos

#### Ejemplo 1
```text
Entrada: prices = [7,1,5,3,6,4]
Salida: 5
Explicación: Compra en el día 2 (precio = 1) y vende en el día 5 (precio = 6), ganancia = 6 - 1 = 5.
Nota que no está permitido comprar en el día 2 y vender en el día 1, ya que debes comprar antes de vender.
```

#### Ejemplo 2
```text
Entrada: prices = [7,6,4,3,1]
Salida: 0
Explicación: En este caso, no se realiza ninguna transacción y la ganancia máxima es 0.
```

### ⚙️ Restricciones

- 1 <= prices.length <= 10⁵
- 0 <= prices[i] <= 10⁴