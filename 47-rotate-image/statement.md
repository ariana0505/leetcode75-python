# 47. Rotate Image / Rotar Imagen

## English

You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

### Examples

#### Example 1
```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
```

#### Example 2
```text
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### Constraints

- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000

---

## Espanol

Se te da una `matrix` 2D de `n x n` que representa una imagen, rota la imagen 90 grados (en sentido horario).

Debes rotar la imagen in place, lo que significa que debes modificar directamente la matriz de entrada. NO asignes otra matriz 2D para hacer la rotacion.

### Ejemplos

#### Ejemplo 1
```text
Entrada: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Salida: [[7,4,1],[8,5,2],[9,6,3]]
```

#### Ejemplo 2
```text
Entrada: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Salida: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
```

### Restricciones

- n == matrix.length == matrix[i].length
- 1 <= n <= 20
- -1000 <= matrix[i][j] <= 1000
