import sys
numCourses = 2
sys.setrecursionlimit(max(sys.getrecursionlimit(), numCourses + 100))
prerequisites = [[1,0],[0,1]]
grafo = [[]for _ in range(numCourses)]
for a,b in prerequisites:
    grafo[a].append(b)

visitados = set()
terminados = set()


def revisar(curso):
    if curso in visitados:
        return False
    if curso in terminados:
        return True
    visitados.add(curso)

    
    for prerequisito in grafo[curso]:
        resultado = revisar(prerequisito)
        if resultado == False:
            return False

    visitados.remove(curso)
    terminados.add(curso)
    return True

for curso in range(numCourses):
    if not revisar(curso):
        print(False)
        break

else :
    print(True)