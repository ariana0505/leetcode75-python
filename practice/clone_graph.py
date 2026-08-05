class Nodo:
    def __init__(self, val, vecinos = None):
        self.val = val
        self.vecinos = vecinos if vecinos is not  None else []

visitados = {} #nodo - > nodo copiado

def clone(nodo:Nodo):

    if nodo == None:
        return 
    if nodo in visitados:
        return visitados[nodo]
    
    copia = Nodo(nodo.val)
    visitados[nodo] = copia

    for vecino in nodo.vecinos:
        copia.vecinos.append(clone(vecino))

    return copia
