import sys

numCourses = 2
sys.setrecursionlimit(3000)
prerequisites = [[1,0]]

terminados = set()
visitados = set()

grafo = [[] for _ in range(numCourses)]

for a,b in prerequisites:
    grafo[a].append(b)

def revisar(curso):
    if curso in visitados:
        return False
    if curso in terminados:
        return True

    visitados.add(curso)
    for requisito in grafo[curso]:
        if not revisar(requisito):
            return False

    visitados.remove(curso)
    terminados.add(curso)

    return True

for curso in range(numCourses):
    if not revisar(curso):
        print(False)
        break
else:
    print(True)