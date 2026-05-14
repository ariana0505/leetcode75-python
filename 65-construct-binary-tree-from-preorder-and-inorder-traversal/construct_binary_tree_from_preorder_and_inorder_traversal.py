class treeNode:
    def __init__(self,val, izq= None, der=  None):
        self.val =  val
        self.izq =  izq
        self.der =  der


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

def builTree(preorder:list ,inorder: list):
    if  not  preorder or not inorder:
        return None
    
    raiz  = treeNode(preorder[0])
    mid = inorder.index(raiz.val)

    raiz.izq =  builTree(preorder[1:mid +1],inorder[:mid])
    raiz.der =  builTree(preorder[mid+1:],inorder[mid +  1:])
    return raiz

tree   =builTree(preorder,inorder)

