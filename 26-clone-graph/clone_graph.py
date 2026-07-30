class Nodo:
    def __init__(self, val = 0, vecinos = None):
        self.val = val
        self.vecinos = vecinos if vecinos is not None else []

visitados = {} #llevaran el orden de nodo, nodo copia 

def cloneGraph(nodo:Nodo):
    if nodo is None:
        return None
    if nodo in visitados:
        return visitados[nodo]

    copia = Nodo(nodo.val)
    visitados[nodo] = copia

    for vecino in nodo.vecinos:
        copia.vecinos.append(cloneGraph(vecino))
    return copia


# caso de prueba: adjList = [[2,4],[1,3],[2,4],[1,3]]
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)

nodo1.vecinos = [nodo2, nodo4]
nodo2.vecinos = [nodo1, nodo3]
nodo3.vecinos = [nodo2, nodo4]
nodo4.vecinos = [nodo1, nodo3]

clon1 = cloneGraph(nodo1)

print("nodo1.val:", nodo1.val, " clon1.val:", clon1.val)
print("misma identidad (debe ser False):", nodo1 is clon1)
print("valores vecinos originales:", [v.val for v in nodo1.vecinos])
print("valores vecinos clonados:  ", [v.val for v in clon1.vecinos])

print()

# caso de prueba: adjList = [[]] (un solo nodo, sin vecinos)
visitados.clear()
nodo_unico = Nodo(1)
clon_unico = cloneGraph(nodo_unico)

print("nodo_unico.val:", nodo_unico.val, " clon_unico.val:", clon_unico.val)
print("misma identidad (debe ser False):", nodo_unico is clon_unico)
print("vecinos clonados (debe ser []):", clon_unico.vecinos)

print()

# caso de prueba: adjList = [] (grafo vacio)
visitados.clear()
clon_vacio = cloneGraph(None)
print("clon de grafo vacio (debe ser None):", clon_vacio)
