cursos = 2
requisitos = [[1, 0], [0, 1]]
grafo = [[] for _ in range(cursos)] # por cada curso crea una lista vacia que tendra los requisitos 

for curso , requisito in requisitos: # por
    grafo[curso].append(requisito)
print(grafo)

visitados = set()
terminados = set()

def revisar_curso(curso):
    if curso in visitados: # lo estamos revisando otra vez: hay ciclo
        return False

    if curso in terminados: # ya fue revisado y sabemos que está bien
        return True

    visitados.add(curso) # empezamos a revisar sus requisitos

    for requisito in grafo[curso]: # reviso i : [req1, req2]
        resultado = revisar_curso(requisito)
        if resultado == False:
            return False
    visitados.remove(curso)
    terminados.add(curso)
    return True

for curso in range(cursos):
    if not revisar_curso(curso): # entra si se encuentra bucle o no se puede hacer
        print(False)
        break
else:
    print(True)