class Treenode:
    def __init__(self,val,  izq = None,  der = None):
        self.val =  val
        self.izq = izq
        self.der = der

maximo  = float('-inf')
def maximum_sum(node):
    global  maximo

    if node == None:
        return 0
    izq = max(maximum_sum(node.izq), 0)
    der = max(maximum_sum(node.der), 0)
    maximo  =  max(node.val+ izq + der, maximo)
    return node.val + max(izq,der)


raiz = Treenode(-10, Treenode(9), Treenode(20, Treenode(15), Treenode(7)))
maximum_sum(raiz)
print(maximo)