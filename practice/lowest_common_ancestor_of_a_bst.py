class  TreeNode:
    def __init__(self, val , izq  = None,der = None):
        self.val = val
        self.izq =  izq
        self.der =  der

node0  =  TreeNode(0)
node2  =  TreeNode(2)
node4  =  TreeNode(4)
node6  =  TreeNode(6)
node8  =  TreeNode(8)
node7  =  TreeNode(7)
node9  =  TreeNode(9)

node6.der  =  node8
node6.izq   =  node2
node2.der =  node4
node2.izq = node0
node8.der= node9
node8.izq =  node7

p=  node7
q=node9
raiz  =  node6

while raiz:
    if raiz.val > q.val and raiz.val  >  p.val:
        raiz  = raiz.izq
    elif raiz.val < q.val and raiz.val  <  p.val:
        raiz =  raiz.der
    else:
        print(raiz.val)
        break