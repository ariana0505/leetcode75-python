## Encode and Decode Strings (English)

Design an algorithm to **encode** a list of strings into a single string and **decode** it back to the original list of strings.

The encoded string is sent over the network and later decoded back to the original list.

### Requirements
- The strings may contain **any of the 256 valid ASCII characters**.
- Your algorithm must correctly handle **all possible characters**, including special symbols such as `:`, `;`, etc.
- **Do not rely on libraries** — the goal is to implement the encoding and decoding logic manually.

### Example 1
**Input:**  
`["lint","code","love","you"]`

**Output:**  
`["lint","code","love","you"]`

**Explanation:**  
One possible encoding method:  
`"lint:;code:;love:;you"`

### Example 2
**Input:**  
`["we", "say", ":", "yes"]`

**Output:**  
`["we", "say", ":", "yes"]`

**Explanation:**  
One possible encoding method:  
`"we:;say:;:::;yes"`

---

## Codificar y Decodificar Cadenas (Español)

Diseña un algoritmo para **codificar** una lista de cadenas en una sola cadena y luego **decodificarla** para obtener la lista original.

La cadena codificada se envía a través de la red y posteriormente se decodifica.

### Requisitos
- Las cadenas pueden contener **cualquiera de los 256 caracteres ASCII válidos**.
- El algoritmo debe manejar correctamente **todo tipo de caracteres**, incluidos símbolos especiales como `:`, `;`, etc.
- **No se deben usar librerías**; el objetivo es implementar la lógica de codificación y decodificación desde cero.

### Ejemplo 1
**Entrada:**  
`["lint","code","love","you"]`

**Salida:**  
`["lint","code","love","you"]`

**Explicación:**  
Un método posible de codificación:  
`"lint:;code:;love:;you"`

### Ejemplo 2
**Entrada:**  
`["we", "say", ":", "yes"]`

**Salida:**  
`["we", "say", ":", "yes"]`

**Explicación:**  
Un método posible de codificación:  
`"we:;say:;:::;yes"`
