# 73. Find Median from Data Stream / Encontrar la Mediana de un Flujo de Datos

## English

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for `arr = [2,3,4]`, the median is `3`.
- For example, for `arr = [2,3]`, the median is `(2 + 3) / 2 = 2.5`.

Implement the `MedianFinder` class:

- `MedianFinder()` initializes the `MedianFinder` object.
- `void addNum(int num)` adds the integer `num` from the data stream to the data structure.
- `double findMedian()` returns the median of all elements so far. Answers within `10^-5` of the actual answer will be accepted.

### Examples

#### Example 1
```text
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Constraints

- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

---

## Espanol

La mediana es el valor central en una lista ordenada de enteros. Si el tamano de la lista es par, no hay un valor central, y la mediana es el promedio de los dos valores centrales.

- Por ejemplo, para `arr = [2,3,4]`, la mediana es `3`.
- Por ejemplo, para `arr = [2,3]`, la mediana es `(2 + 3) / 2 = 2.5`.

Implementa la clase `MedianFinder`:

- `MedianFinder()` inicializa el objeto `MedianFinder`.
- `void addNum(int num)` agrega el entero `num` del flujo de datos a la estructura de datos.
- `double findMedian()` devuelve la mediana de todos los elementos hasta el momento. Se aceptaran respuestas dentro de `10^-5` de la respuesta real.

### Ejemplos

#### Ejemplo 1
```text
Entrada:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Salida:
[null, null, null, 1.5, null, 2.0]

Explicacion:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // devuelve 1.5 (es decir, (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // devuelve 2.0
```

### Restricciones

- -10^5 <= num <= 10^5
- Habra al menos un elemento en la estructura de datos antes de llamar a findMedian.
- Se haran como maximo 5 * 10^4 llamadas a addNum y findMedian.
