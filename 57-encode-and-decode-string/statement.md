# 57. Encode and Decode Strings / Codificar y Decodificar Cadenas

## English

Design an algorithm to **encode** a list of strings into a single string and **decode** it back to the original list of strings.

The encoded string is sent over the network and later decoded back to the original list.

### Requirements

- The strings may contain **any of the 256 valid ASCII characters**.
- Your algorithm must correctly handle **all possible characters**, including special symbols such as `:`, `;`, etc.
- **Do not rely on libraries** -- the goal is to implement the encoding and decoding logic manually.

### Examples

#### Example 1
```text
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation: One possible encoding method: "lint:;code:;love:;you"
```

#### Example 2
```text
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation: One possible encoding method: "we:;say:;:::;yes"
```

---

## Espanol

Disena un algoritmo para **codificar** una lista de cadenas en una sola cadena y luego **decodificarla** para obtener la lista original.

La cadena codificada se envia a traves de la red y posteriormente se decodifica.

### Requisitos

- Las cadenas pueden contener **cualquiera de los 256 caracteres ASCII validos**.
- El algoritmo debe manejar correctamente **todo tipo de caracteres**, incluidos simbolos especiales como `:`, `;`, etc.
- **No se deben usar librerias**; el objetivo es implementar la logica de codificacion y decodificacion desde cero.

### Ejemplos

#### Ejemplo 1
```text
Entrada: ["lint","code","love","you"]
Salida: ["lint","code","love","you"]
Explicacion: Un metodo posible de codificacion: "lint:;code:;love:;you"
```

#### Ejemplo 2
```text
Entrada: ["we", "say", ":", "yes"]
Salida: ["we", "say", ":", "yes"]
Explicacion: Un metodo posible de codificacion: "we:;say:;:::;yes"
```
