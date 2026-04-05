class treeNode:
    def __init__(self,  valor, izq = None, der = None):
        self.valor = valor
        self.izq =izq
        self.der = der

root1 = treeNode(2,treeNode(1),treeNode(3))
root2 = treeNode(2,treeNode(3),treeNode(1))

def esValido(nodo, min  = float('-inf'), max = float('inf')):
    if not nodo:
        return   True
    if nodo.valor <= min  or nodo.valor >= max:
        return False
    return esValido(nodo.izq, min , nodo.valor)  and esValido(nodo.der,  nodo.valor, max)

print(esValido(root1))  # True
print(esValido(root2))  # False
