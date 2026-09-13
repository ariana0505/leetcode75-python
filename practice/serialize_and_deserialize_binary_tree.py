import sys
class TreeNodo:
    def __init__(self,val = 0,der = None, izq = None):
        self.val = val
        self.der = der
        self.izq = izq

nodo = TreeNodo(1,TreeNodo(2),TreeNodo(3,TreeNodo(4),TreeNodo(6)))

sys.setrecursionlimit(max(sys.getrecursionlimit(), 20_000))

def serializar(nodo):
    lista =[]
    def dfs(nodo:TreeNodo):
        if nodo is None:
            lista.append("N")
            return 
        lista.append(str(nodo.val))
        dfs(nodo.izq)
        dfs(nodo.der)

    dfs(nodo)
    return ",".join(lista)

def deserializar(text:str):
    valores = iter(text.split(","))
    def dfs():
        valor = next(valores)
        if valor == "N":
            return None
        nodo = TreeNodo(int(valor))
        nodo.izq = dfs()
        nodo.der = dfs()
        return nodo
    return dfs()

