class treeNode:
    def __init__(self,  valor, izq = None, der = None):
        self.valor = valor
        self.izq =izq
        self.der = der

root1 = treeNode(2,treeNode(1),treeNode(3))
root2 = treeNode(2,treeNode(3),treeNode(1))


