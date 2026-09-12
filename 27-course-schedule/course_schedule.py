# Cantidad total de cursos
numCourses = 2

# [curso, requisito]
# Para realizar el curso 1, primero necesito completar el curso 0
prerequisites = [[1, 0], [0, 1]]


# Crea una lista vacía para guardar los requisitos de cada curso
# Con 2 cursos inicialmente tenemos: [[], []]
grafo = [[] for _ in range(numCourses)]


# Construimos el grafo
for curso, requisito in prerequisites:
    # Guardamos qué requisito necesita cada curso
    grafo[curso].append(requisito)


# Cursos que forman parte del recorrido DFS actual
# Si volvemos a encontrar uno de estos cursos, existe un ciclo
proceso = set()

# Cursos que ya revisamos completamente y sabemos que son seguros
terminados = set()


def revisar(curso):
      # Si encontramos nuevamente un curso del recorrido actual,
      # significa que regresamos al mismo punto y existe un ciclo
      if curso in proceso:
          return False

      # Si el curso ya fue revisado completamente,
      # no necesitamos volver a revisar sus requisitos
      if curso in terminados:
          return True

      # Marcamos que estamos comenzando a revisar este curso
      proceso.add(curso)

      # Recorremos todos los requisitos del curso actual
      for requisito in grafo[curso]:

          # Revisamos recursivamente cada requisito
          # Si alguno tiene un ciclo, este curso tampoco puede completarse
          if not revisar(requisito):
              return False

      # Terminamos de revisar el curso, así que lo retiramos
      # de la ruta DFS actual
      proceso.remove(curso)

      # Lo guardamos como completamente revisado y seguro
      terminados.add(curso)

      return True


  # Debemos comprobar todos los cursos, porque el grafo
  # puede tener varias partes separadas
for curso in range(numCourses):

    # Si algún curso contiene un ciclo, no podemos terminarlos todos
    if not revisar(curso):
        print(False)
        break
else:
    # Este else pertenece al for y se ejecuta únicamente
    # cuando el ciclo termina sin ejecutar break
    print(True)