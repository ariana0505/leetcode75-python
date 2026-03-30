class TreeNode:
    def __init__(self, valor ,izquierda= None, derecha=None):
        self.valor = valor
        self.derecha = derecha
        self.izquierda = izquierda


def is_same(a: TreeNode,b:TreeNode):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return (a.valor == b.valor and
            is_same(a.izquierda, b.izquierda) and
            is_same(a.derecha, b.derecha))


def is_subtree(tree, subtree):
    if not tree:
        return False
    if is_same(tree,subtree):
        return True
    return (is_subtree(tree.izquierda, subtree) or is_subtree(tree.derecha, subtree))

root1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root1, sub1))  # True

# Example 2: root = [3,4,5,1,2(->0),null,null], subRoot = [4,1,2] -> false
root2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
sub2 = TreeNode(4, TreeNode(1), TreeNode(2))
print(is_subtree(root2, sub2))  # False
