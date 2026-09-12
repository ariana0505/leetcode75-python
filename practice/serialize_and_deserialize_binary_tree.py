class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Ejemplo 1: k=1 -> esperado: 1
#     3
#    / \
#   1   4
#    \
#     2
node2 = TreeNode(2)
node1 = TreeNode(1, right=node2)
node4 = TreeNode(4)
node3 = TreeNode(3, left=node1, right=node4)

def serializar(nodo:TreeNode,):
    lista = []
    def recorrer(nodo):
        if nodo is None:
            lista.append("N")
            return 
        lista.append(str(nodo.val))

        recorrer(nodo.left)
        recorrer(nodo.right)
    
    recorrer(nodo)
    return ",".join(lista)

def deserializacion(texto:str):
    valores = iter(texto.split(","))

    def recorrer():
        valor = next(valores)

        if valor == "N":
            return None

        nodo = TreeNode(int(valor))
        nodo.left = recorrer()
        nodo.right = recorrer()
        return nodo
    return recorrer()