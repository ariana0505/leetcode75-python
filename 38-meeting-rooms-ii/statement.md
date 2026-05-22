# 38. Meeting Rooms II / Salas de Reuniones II

## English

Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of conference rooms required.

### Examples

#### Example 1
```text
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Explanation: We need two rooms: one for [0,30] and another for [5,10] and [15,20].
```

#### Example 2
```text
Input: intervals = [[7,10],[2,4]]
Output: 1
Explanation: The two meetings do not overlap, so one room is enough.
```

### Constraints

- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6

---

## Espanol

Dado un arreglo de intervalos de reuniones `intervals` donde `intervals[i] = [starti, endi]`, devuelve el numero minimo de salas de conferencias necesarias.

### Ejemplos

#### Ejemplo 1
```text
Entrada: intervals = [[0,30],[5,10],[15,20]]
Salida: 2
Explicacion: Se necesitan dos salas: una para [0,30] y otra para [5,10] y [15,20].
```

#### Ejemplo 2
```text
Entrada: intervals = [[7,10],[2,4]]
Salida: 1
Explicacion: Las dos reuniones no se superponen, asi que basta con una sala.
```

### Restricciones

- 1 <= intervals.length <= 10^4
- 0 <= starti < endi <= 10^6
