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

def serializar(arbol:tree):
    valores = []
    def recorrer(arbol:tree):
        if arbol is None:
            valores.append("N")
            return
        valores.append(str(arbol.val))
        recorrer(arbol.izq)
        recorrer(arbol.der)
    recorrer(arbol)
    return ";".join(valores)

def deserilizar(texto:str):
    valores = iter(texto.split(";"))
    def construir():
        valor = next(valores)

        if valor == "N":
            return None
        
        
        nodo = tree(int(valor))
        nodo.izq = (construir())
        nodo.der = (construir())
        return nodo
    return construir()