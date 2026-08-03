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

def invert(node: tree):
    if node is None:
        return
    temp = node.izq
    node.izq = node.der
    node.der = temp

    invert(node.der)
    invert(node.izq)