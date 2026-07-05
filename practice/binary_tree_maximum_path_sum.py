class Treenode:
    def __init__(self,  val , izq=None , der = None):
        self.val  =  val
        self.izq = izq
        self.der  = der

arbol = Treenode(-10,Treenode(9),Treenode(20,Treenode(15),Treenode(7)))
raiz  = arbol
maximo = float('-inf')
def  maximun_sum(node):
    global maximo
    if node is None:
        return 0
    izq = max(maximun_sum(node.izq),0)
    der = max(maximun_sum(node.der),0)

    maximo = max(maximo,node.val + izq + der)
    return node.val + max(izq,der)

maximun_sum(raiz)
print(maximo)