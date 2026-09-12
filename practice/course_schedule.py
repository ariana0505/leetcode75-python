cursos = 2
requisitos = [[1, 0], [0, 1]]
# Paso 1: crea una lista de requisitos para cada curso.
grafo = [[] for _ in range(cursos)]

# Paso 2: conecta cada curso con los cursos que debe completar antes.
for curso , requisito in requisitos:
    grafo[curso].append(requisito)
print(grafo)

# `visitados` sigue la ruta actual; `terminados` guarda cursos ya validados.
visitados = set()
terminados = set()

def revisar_curso(curso):
    # Paso 3: si reaparece en la ruta actual, encontramos un ciclo.
    if curso in visitados:
        return False

    # Un curso terminado no necesita volver a recorrerse.
    if curso in terminados:
        return True

    # Marca el curso como parte de la ruta que estamos explorando.
    visitados.add(curso)

    # Paso 4: valida recursivamente todos sus requisitos.
    for requisito in grafo[curso]:
        resultado = revisar_curso(requisito)
        if resultado == False:
            return False

    # Al terminar la rama, quita el curso de la ruta y memoriza el resultado.
    visitados.remove(curso)
    terminados.add(curso)
    return True

# Paso 5: comprueba cada curso para cubrir también grafos desconectados.
for curso in range(cursos):
    if not revisar_curso(curso):
        print(False)
        break
else:
    print(True)
