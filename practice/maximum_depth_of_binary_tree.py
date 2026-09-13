class TreeNodo:
    def __init__(self,val = 0,der = None, izq = None):
        self.val = val
        self.der = der
        self.izq = izq

nodo = TreeNodo(1,TreeNodo(2),TreeNodo(3,TreeNodo(4),TreeNodo(6)))

def maximum_depth(nodo:TreeNodo):
    if nodo is None:
        return 0

    izq = maximum_depth(nodo.izq)
    der = maximum_depth(nodo.izq)

    return max(izq, der ) + 1 