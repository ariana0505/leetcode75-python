# 53. Valid Parentheses / Parentesis Validos

## English

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

### Examples

#### Example 1
```text
Input: s = "()"
Output: true
```

#### Example 2
```text
Input: s = "()[]{}"
Output: true
```

#### Example 3
```text
Input: s = "(]"
Output: false
```

#### Example 4
```text
Input: s = "([])"
Output: true
```

### Constraints

- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.

---

## Espanol

Dada una cadena `s` que contiene unicamente los caracteres `'('`, `')'`, `'{'`, `'}'`, `'['` y `']'`, determina si la cadena de entrada es valida.

Una cadena de entrada es valida si:

1. Los parentesis de apertura deben cerrarse con el mismo tipo de parentesis.
2. Los parentesis de apertura deben cerrarse en el orden correcto.
3. Cada parentesis de cierre tiene su correspondiente parentesis de apertura del mismo tipo.

### Ejemplos

#### Ejemplo 1
```text
Entrada: s = "()"
Salida: true
```

#### Ejemplo 2
```text
Entrada: s = "()[]{}"
Salida: true
```

#### Ejemplo 3
```text
Entrada: s = "(]"
Salida: false
```

#### Ejemplo 4
```text
Entrada: s = "([])"
Salida: true
```

### Restricciones

- 1 <= s.length <= 10^4
- s contiene unicamente los parentesis '()[]{}'.
