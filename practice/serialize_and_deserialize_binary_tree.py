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

cabeza = root
def serialize(root):
    valores = []

    def recorrer(nodo):
        if nodo is None:
            valores.append("N")
            return
        valores.append(str(nodo.val))
        recorrer(nodo.izq)
        recorrer(nodo.der)
    recorrer(root)
    return ",".join(valores)

def deserialize(datos):
    valores = iter(datos.split(","))
    def construir():
          valor = next(valores)

          if valor == "N":
              return None

          nodo = tree(int(valor))
          nodo.izq = construir()
          nodo.der = construir()

          return nodo

    return construir()