class TreeNode:
    def  __init__(self, val,izq =  None, der = None):
        self.val = val
        self.izq = izq
        self.der = der

node1 =  TreeNode(3)
node2 = TreeNode(9)
node3    =   TreeNode(20)
node4  =  TreeNode(15)
node5 = TreeNode(7)

node1.der = node3
node1.izq = node2
node3.der = node5
node3.izq =  node4

resultado  = []
procesador =  [node1]

while procesador:
    nivel = []
    for _  in range(len(procesador)):
        nodo  = procesador.pop(0)
        nivel.append(nodo.val)
        if  nodo.izq:
            procesador.append(nodo.izq)
        if nodo.der:
            procesador.append(nodo.der)
    resultado.append(nivel)
print(resultado)