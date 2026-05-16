class TreeNode:
    def __init__(self, val, izq=None, der=None):
        self.val = val
        self.izq = izq
        self.der = der

node1 = TreeNode(3)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node1.der = node3
node1.izq = node2
node3.der = node5
node3.izq = node4

resultado = []
procesador = [node1]

while procesador:
    nivel = []
    for _ in range(len(procesador)):
        extraido = procesador.pop(0)
        nivel.append(extraido.val)
        if extraido.izq:
            procesador.append(extraido.izq)
        if extraido.der:
            procesador.append(extraido.der)

    resultado.append(nivel)
print(resultado)
