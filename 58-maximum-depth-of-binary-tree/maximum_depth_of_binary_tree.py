class TreeNode:
    def __init__(self, val=0, izq=None, der=None):
        self.val = val
        self.izq = izq
        self.der = der

root = TreeNode(4)
root.izq = TreeNode(2)
root.der = TreeNode(7)
root.izq.izq = TreeNode(1)
root.izq.der = TreeNode(3)
root.der.izq = TreeNode(6)
root.der.der = TreeNode(9)


def maximun(nodo:TreeNode):
    if nodo == None:
        return 0
    R = maximun(nodo.der)
    L = maximun(nodo.izq)
    return 1 + max(L,R)

print(maximun(root))