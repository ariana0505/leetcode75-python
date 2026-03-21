# 10. Container With Most Water / Contenedor con mas agua

## English

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the *i-th* line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the **most water**.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

### Examples

#### Example 1
```text
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The maximum area of water the container can store is 49.
```

#### Example 2
```text
Input: height = [1,1]
Output: 1
```

### Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Espanol

Se te da un arreglo de enteros `height` de longitud `n`. Hay `n` lineas verticales dibujadas de tal forma que los dos extremos de la linea *i-esima* son `(i, 0)` y `(i, height[i])`.

Encuentra dos lineas que, junto con el eje x, formen un contenedor que pueda **almacenar la mayor cantidad de agua**.

Devuelve la cantidad maxima de agua que el contenedor puede almacenar.

**Nota:** No puedes inclinar el contenedor.

### Ejemplos

#### Ejemplo 1
```text
Entrada: height = [1,8,6,2,5,4,8,3,7]
Salida: 49
Explicacion: El area maxima que puede almacenar el contenedor es 49.
```

#### Ejemplo 2
```text
Entrada: height = [1,1]
Salida: 1
```

### Restricciones

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`
