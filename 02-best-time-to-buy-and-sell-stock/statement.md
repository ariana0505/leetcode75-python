# 3. Best Time to Buy and Sell Stock / Mejor Momento para Comprar y Vender Acciones

## English

You are given an array `prices` where `prices[i]` is the price of a given stock on the *i-th* day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return `0`.

### Examples

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

### Constraints

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

---

## Espanol

Se te da un arreglo `prices` donde `prices[i]` es el precio de una accion en el dia *i*.

Deseas maximizar tu ganancia eligiendo un dia para comprar una accion y un dia diferente en el futuro para venderla.

Devuelve la maxima ganancia que puedes obtener de esta transaccion.
Si no puedes obtener ninguna ganancia, devuelve `0`.

### Ejemplos

#### Ejemplo 1
```text
Entrada: prices = [7,1,5,3,6,4]
Salida: 5
Explicacion: Compra en el dia 2 (precio = 1) y vende en el dia 5 (precio = 6), ganancia = 6 - 1 = 5.
Nota que no esta permitido comprar en el dia 2 y vender en el dia 1, ya que debes comprar antes de vender.
```

#### Ejemplo 2
```text
Entrada: prices = [7,6,4,3,1]
Salida: 0
Explicacion: En este caso, no se realiza ninguna transaccion y la ganancia maxima es 0.
```

### Restricciones

- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
