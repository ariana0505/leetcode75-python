# 24. Unique Paths / Caminos Unicos

## English

There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 10^9`.

### Examples

#### Example 1
```text
Input: m = 3, n = 7
Output: 28
```

#### Example 2
```text
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

### Constraints

- 1 <= m, n <= 100

---

## Espanol

Hay un robot en una cuadricula de `m x n`. El robot esta inicialmente ubicado en la esquina superior izquierda (es decir, `grid[0][0]`). El robot intenta moverse a la esquina inferior derecha (es decir, `grid[m - 1][n - 1]`). El robot solo puede moverse hacia abajo o hacia la derecha en cualquier momento.

Dados los dos enteros `m` y `n`, devuelve el numero de caminos unicos posibles que el robot puede tomar para llegar a la esquina inferior derecha.

Los casos de prueba se generan de modo que la respuesta sea menor o igual a `2 * 10^9`.

### Ejemplos

#### Ejemplo 1
```text
Entrada: m = 3, n = 7
Salida: 28
```

#### Ejemplo 2
```text
Entrada: m = 3, n = 2
Salida: 3
Explicacion: Desde la esquina superior izquierda, hay un total de 3 formas de llegar a la esquina inferior derecha:
1. Derecha -> Abajo -> Abajo
2. Abajo -> Abajo -> Derecha
3. Abajo -> Derecha -> Abajo
```

### Restricciones

- 1 <= m, n <= 100
