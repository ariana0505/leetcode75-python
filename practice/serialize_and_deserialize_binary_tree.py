import sys
class tree:
    def __init__(self, val , izq = None, der = None):
        self.val = val
        self.izq = izq
        self.der = der

# Arbol del ejemplo 1: [4,2,7,1,3,6,9]
root = tree(4)
root.izq = tree(2)
root.der = tree(7)
root.izq.izq = tree(1)
root.izq.der = tree(3)
root.der.izq = tree(6)
root.der.der = tree(9)

cur = root
sys.setrecursionlimit(20_000)
def serialize(raiz):
    lista = []
    def agregar(nodo:tree):
        if nodo is None:
            lista.append("N")
            return
        lista.append(str(nodo.val))
        agregar(nodo.izq)
        agregar(nodo.der)

    agregar(raiz)
    return ",".join(lista)
def deserializar(text:str):
    valores = iter(text.split(","))
    def crear():
        valor = next(valores)
        if valor == "N":
            return None
        nodo = tree(int(valor))
        nodo.izq = crear()
        nodo.der = crear()
        return nodo
    arbol = crear()
    return arbol

