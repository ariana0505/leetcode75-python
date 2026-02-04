## Insert Interval (English)

You are given an array of **non-overlapping intervals** `intervals`, where `intervals[i] = [start_i, end_i]` represents the start and end of the *i-th* interval.  
The array is sorted in **ascending order by `start_i`**.

You are also given an interval `newInterval = [start, end]`.

Insert `newInterval` into `intervals` such that:
- The result is still sorted by start time.
- There are **no overlapping intervals** (merge overlaps if necessary).

Return the resulting array after insertion.

**Note:** You do not need to modify `intervals` in-place. You may create and return a new array.

### Example 1
**Input:**  
`intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`  

**Output:**  
`[[1,5],[6,9]]`

### Example 2
**Input:**  
`intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`  

**Output:**  
`[[1,2],[3,10],[12,16]]`

**Explanation:**  
The new interval `[4,8]` overlaps with `[3,5]`, `[6,7]`, and `[8,10]`.

### Constraints
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` is sorted by `start_i` in ascending order
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`

---

## Insertar Intervalo (Español)

Se te da un arreglo de **intervalos no superpuestos** `intervals`, donde `intervals[i] = [start_i, end_i]` representa el inicio y fin del *i-ésimo* intervalo.  
El arreglo está ordenado en **orden ascendente por `start_i`**.

También se te da un intervalo `newInterval = [start, end]`.

Inserta `newInterval` en `intervals` de modo que:
- El resultado siga ordenado por el inicio.
- No existan **intervalos superpuestos** (fusiona los intervalos que se superpongan).

Devuelve el arreglo resultante después de la inserción.

**Nota:** No es necesario modificar `intervals` en el lugar. Puedes crear y devolver un nuevo arreglo.

### Ejemplo 1
**Entrada:**  
`intervals = [[1,3],[6,9]]`, `newInterval = [2,5]`  

**Salida:**  
`[[1,5],[6,9]]`

### Ejemplo 2
**Entrada:**  
`intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4,8]`  

**Salida:**  
`[[1,2],[3,10],[12,16]]`

**Explicación:**  
El nuevo intervalo `[4,8]` se superpone con `[3,5]`, `[6,7]` y `[8,10]`.

### Restricciones
- `0 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^5`
- `intervals` está ordenado por `start_i` en orden ascendente
- `newInterval.length == 2`
- `0 <= start <= end <= 10^5`
