class  treeNode:
    def __init__(self,valor,izquierda= None,derecha = None):
        self.valor = valor
        self.derecha = derecha
        self.izquierda  = izquierda

tree = treeNode(4,treeNode(6,treeNode(7),treeNode(8)),treeNode(8,treeNode(3),treeNode(1)))
subtree = treeNode(6,treeNode(7),treeNode(8))

def isSame(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2 or t1.valor != t2.valor:
        return False
    return(isSame(t1.derecha,t2.derecha) and isSame(t1.izquierda,t2.izquierda))

def isSubtree(root,subroot):
    if not root:
        return  False
    if isSame(root,subroot):
        return True
    return(isSubtree(root.derecha,subroot) or isSubtree(root.izquierda, subroot))

print(isSubtree(tree,subtree))