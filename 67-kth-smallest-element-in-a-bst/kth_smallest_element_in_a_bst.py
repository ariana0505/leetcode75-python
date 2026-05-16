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
node2 = TreeNode(2)
node1 = TreeNode(1, right=node2)
node4 = TreeNode(4)
node3 = TreeNode(3, left=node1, right=node4)

raiz = node3
k = 1
n = 0 # numero de elementos que visitamos
stack = []  
cur = raiz

while cur or  stack:
    while cur:
        stack.append(cur)
        cur = cur.left
    
    cur = stack.pop()
    n +=  1
    if  k  == n:
        print(cur.val)
        break
    cur = cur.right
    