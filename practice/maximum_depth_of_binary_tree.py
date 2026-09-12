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

def maximum_depth(nodo:TreeNode):
    # 1. Un árbol vacío no aporta niveles a la profundidad.
    if nodo is None:
        return 0

    # 2. Calculamos recursivamente la profundidad de cada subárbol.
    izquierda = maximum_depth(nodo.left) 
    derecha = maximum_depth(nodo.right) 

    # 3. Elegimos la rama más profunda y sumamos el nodo actual.
    return max(izquierda,derecha) + 1

print(maximum_depth(node3))
