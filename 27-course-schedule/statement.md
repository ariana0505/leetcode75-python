# 27. Course Schedule / Calendario de Cursos

## English

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

- For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

### Examples

#### Example 1
```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
```

#### Example 2
```text
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should
also have finished course 1. So it is impossible.
```

### Constraints

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique.

---

## Espanol

Hay un total de `numCourses` cursos que debes tomar, etiquetados de `0` a `numCourses - 1`. Se te da un arreglo `prerequisites` donde `prerequisites[i] = [ai, bi]` indica que debes tomar primero el curso `bi` si quieres tomar el curso `ai`.

- Por ejemplo, el par `[0, 1]` indica que para tomar el curso `0` debes tomar primero el curso `1`.

Devuelve `true` si puedes terminar todos los cursos. En caso contrario, devuelve `false`.

### Ejemplos

#### Ejemplo 1
```text
Entrada: numCourses = 2, prerequisites = [[1,0]]
Salida: true
Explicacion: Hay un total de 2 cursos para tomar.
Para tomar el curso 1 debes haber terminado el curso 0. Entonces es posible.
```

#### Ejemplo 2
```text
Entrada: numCourses = 2, prerequisites = [[1,0],[0,1]]
Salida: false
Explicacion: Hay un total de 2 cursos para tomar.
Para tomar el curso 1 debes haber terminado el curso 0, y para tomar el curso 0
tambien debes haber terminado el curso 1. Entonces es imposible.
```

### Restricciones

- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- Todos los pares prerequisites[i] son unicos.
