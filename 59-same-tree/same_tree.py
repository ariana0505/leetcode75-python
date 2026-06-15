class treeNode:
    def   __init__(self,val, izq =None, der=None):
        self.val = val
        self.izq =izq
        self.der =  der

arbol1 = treeNode(1,treeNode(2),treeNode(3))
arbol2 = treeNode(1,treeNode(2),treeNode(3))

def  isSame(arbol1,arbol2):
    if not arbol1 and not arbol2:
        return True
    if not arbol1 or not arbol2:
        return False
    if arbol1.val != arbol2.val:
        return False
    return (isSame(arbol1.izq, arbol2.izq) and
            isSame(arbol1.der, arbol2.der))

print(isSame(arbol1, arbol2))