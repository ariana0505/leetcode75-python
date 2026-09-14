import sys
sys.setrecursionlimit(20000)
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

def serializar(nodo:tree):
    lista = []
    def agregar(cur:tree):
        if cur is None:
            lista.append("N")
            return
        lista.append(str(cur.val))
        agregar(cur.izq)
        agregar(cur.der)
    agregar(nodo)
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
    return crear()