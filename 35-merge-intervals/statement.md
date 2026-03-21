# 35. Merge Intervals / Intervalos de Fusion

## English

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

### Examples

#### Example 1
```text
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
```

#### Example 2
```text
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

### Constraints

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4

---

## Espanol

Dado un arreglo de `intervals` donde `intervals[i] = [starti, endi]`, fusiona todos los intervalos superpuestos y devuelve un arreglo de intervalos no superpuestos que cubran todos los intervalos de la entrada.

### Ejemplos

#### Ejemplo 1
```text
Entrada: intervals = [[1,3],[2,6],[8,10],[15,18]]
Salida: [[1,6],[8,10],[15,18]]
Explicacion: Como los intervalos [1,3] y [2,6] se superponen, se fusionan en [1,6].
```

#### Ejemplo 2
```text
Entrada: intervals = [[1,4],[4,5]]
Salida: [[1,5]]
Explicacion: Los intervalos [1,4] y [4,5] se consideran superpuestos.
```

### Restricciones

- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti <= endi <= 10^4
