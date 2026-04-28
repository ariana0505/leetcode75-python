class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Ejemplo 1: k=1 -> esperado: 1
#     3
#    / \
#   1   4
#    \
#     2
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)

node1.right = node2
node3.left = node1
node3.right = node4

root = node3
k = 1
r = []

def smallest_element(nodo: TreeNode):
    if not nodo:
        return
    smallest_element(nodo.left)   # 1. va al más pequeño primero
    r.append(nodo.val)            # 2. agrega el nodo actual
    smallest_element(nodo.right)  # 3. luego los más grandes

smallest_element(root)
print(r[k - 1])
