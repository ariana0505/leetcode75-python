class TreeNode:
    def __init__(self, val, izq=None, der=None):
        self.val = val
        self.izq = izq
        self.der = der


def max_path_sum(raiz):
    maximo = float('-inf')

    def gain(node):
        nonlocal maximo
        if node is None:
            return 0
        izq = max(gain(node.izq), 0)
        der = max(gain(node.der), 0)
        maximo = max(maximo, node.val + izq + der)
        return node.val + max(izq, der)

    gain(raiz)
    return maximo


arbol = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_path_sum(arbol))