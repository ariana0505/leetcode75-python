# 36. Non-overlapping Intervals / Intervalos No Superpuestos

## English

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

### Examples

#### Example 1
```text
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

#### Example 2
```text
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

#### Example 3
```text
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
```

### Constraints

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

---

## Espanol

Dado un arreglo de intervalos `intervals` donde `intervals[i] = [starti, endi]`, devuelve el numero minimo de intervalos que necesitas eliminar para que el resto de los intervalos no se superpongan.

### Ejemplos

#### Ejemplo 1
```text
Entrada: intervals = [[1,2],[2,3],[3,4],[1,3]]
Salida: 1
Explicacion: [1,3] puede eliminarse y el resto de los intervalos no se superponen.
```

#### Ejemplo 2
```text
Entrada: intervals = [[1,2],[1,2],[1,2]]
Salida: 2
Explicacion: Necesitas eliminar dos [1,2] para que el resto de los intervalos no se superponga.
```

#### Ejemplo 3
```text
Entrada: intervals = [[1,2],[2,3]]
Salida: 0
Explicacion: No necesitas eliminar ningun intervalo ya que no se superponen.
```

### Restricciones

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4
