class Treenode:
    def __init__(self,valor,izquierda = None,derecha= None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

tree =  Treenode(4, Treenode(5,Treenode(6),Treenode(9)),Treenode(8,Treenode(7),Treenode(6)))
subtree = Treenode(5,Treenode(6),Treenode(9))
prueba = Treenode(5,Treenode(7),Treenode(9))
def isSame(root,subroot):
    if not root and not subroot:
        return  True
    if not root or not subroot or root.valor != subroot.valor:
        return False
    return ( isSame(root.izquierda, subroot.izquierda) and  isSame(root.derecha ,  subroot.derecha))

print(isSame(subtree, prueba))

