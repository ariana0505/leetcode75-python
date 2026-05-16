class TreeNode:
    def __init__(self, val, izq=None, der=None):
        self.val = val
        self.izq = izq
        self.der = der

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

def build(preorder: list, inorder: list):
    if not preorder or not inorder:
        return None

    raiz = TreeNode(preorder[0])
    mid = inorder.index(raiz.val)

    raiz.izq = build(preorder[1:mid + 1], inorder[:mid])
    raiz.der = build(preorder[mid + 1:], inorder[mid + 1:])
    return raiz

tree = build(preorder, inorder)
print(tree.val, tree.izq.val, tree.der.val)
