class Node:
    def __init__(self,val,vecinos = None):
        self.val = val
        self.vecinos = vecinos if vecinos is not None else []

visitados = {} # nodo : nodo copia
def clone_graph(nodo : Node):
    if not nodo:
        return None
    if nodo in visitados:
        return visitados[nodo]
    visitados[nodo] = Node(nodo.val) # -> nodo : nodo copia (SIN VECINOS)
    copi = visitados[nodo]

    #OBTENEMOS VECINOS

    for vecino in nodo.vecinos:
        copi.vecinos.append(clone_graph(vecino))

    return copi