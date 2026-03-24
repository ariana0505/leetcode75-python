class TreeNode:
    def __init__(self, valor, derecha=None , izquierda= None):
        self.valor = valor
        self.derecha = derecha
        self.izquierda = izquierda


tree = TreeNode(3,TreeNode(4,8,9),TreeNode(6,5,3))
subtree = TreeNode(6,5,3)


