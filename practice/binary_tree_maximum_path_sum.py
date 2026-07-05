class TreeNode:
    def __init__(self, val, izq=None, der=None):
        self.val = val
        self.izq = izq
        self.der = der

arbol = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
raiz =  arbol
maximo = float('-inf')

def  maximum_path_sum(node):
    global  maximo
    if node == None:
        return 0
    izq = max(maximum_path_sum(node.izq),0)
    der = max(maximum_path_sum(node.der),0)
    maximo  = max(maximo,  node.val+izq+der)
    return node.val + max(der,izq)

maximum_path_sum(raiz)
print(maximo)