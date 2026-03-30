class TreeNode:
    def __init__(self, valor ,izquierda= None, derecha=None):
        self.valor = valor
        self.derecha = derecha
        self.izquierda = izquierda

def isValidBST(root, lo=float('-inf'),hi= float('inf')):
    if not root :
        return True
    if not (lo < root.valor < hi):
        return False
    return(isValidBST(root.izquierda, lo ,root.valor) and isValidBST(root.derecha,root.valor, hi))

# BST valido: [2, 1, 3]
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
print(isValidBST(root1))  # True

# No valido: [5, 1, 4, null, null, 3, 6] - el 3 esta en subarbol derecho de 5 pero es < 5
root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(isValidBST(root2))  # False

# Un solo nodo
root3 = TreeNode(1)
print(isValidBST(root3))  # True

# No valido: [5, 4, 6, null, null, 3, 7] - el 3 es hijo izq de 6 pero < 5
root4 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
print(isValidBST(root4))  # False

# BST valido mas grande: [10, 5, 15, 3, 7, 12, 20]
root5 = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, TreeNode(12), TreeNode(20)))
print(isValidBST(root5))  # True
