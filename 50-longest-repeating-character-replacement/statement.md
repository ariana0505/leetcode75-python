## Longest Repeating Character Replacement (English)

You are given a string `s` and an integer `k`.  
You can choose any character in the string and change it to any other **uppercase English letter**. You may perform this operation **at most `k` times**.

Return the **length of the longest substring** containing the same letter that you can obtain after performing the operations.

### Example 1
**Input:** `s = "ABAB"`, `k = 2`  
**Output:** `4`  

**Explanation:**  
Replace the two `'A'` characters with `'B'` (or vice versa) to get a substring of length `4` with the same letter.

### Example 2
**Input:** `s = "AABABBA"`, `k = 1`  
**Output:** `4`  

**Explanation:**  
Replace the `'A'` in the middle with `'B'` to form `"AABBBBA"`.  
The substring `"BBBB"` has length `4`, which is the maximum.

---

## Reemplazo del Carácter Repetido Más Largo (Español)

Se te da una cadena `s` y un entero `k`.  
Puedes elegir cualquier carácter de la cadena y cambiarlo por cualquier **letra mayúscula del alfabeto inglés**. Puedes realizar esta operación **como máximo `k` veces**.

Devuelve la **longitud de la subcadena más larga** que contenga la misma letra después de realizar las operaciones.

### Ejemplo 1
**Entrada:** `s = "ABAB"`, `k = 2`  
**Salida:** `4`  

**Explicación:**  
Reemplaza las dos `'A'` por `'B'` (o viceversa) para obtener una subcadena de longitud `4` con la misma letra.

### Ejemplo 2
**Entrada:** `s = "AABABBA"`, `k = 1`  
**Salida:** `4`  

**Explicación:**  
Reemplaza la `'A'` del medio por `'B'` para formar `"AABBBBA"`.  
La subcadena `"BBBB"` tiene longitud `4`, que es el máximo.
