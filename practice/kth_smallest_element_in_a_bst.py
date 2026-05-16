class TreeNode:
    def __init__(self, val, izq=None, der=None):
        self.val = val
        self.izq = izq
        self.der = der


# Hojas del nivel más bajo
nodo0 = TreeNode(0)
nodo2 = TreeNode(2)

# Nodo 1 con hijos 0 y 2
nodo1 = TreeNode(1, izq=nodo0, der=nodo2)

# Hoja 4
nodo4 = TreeNode(4)

# Nodo 3 con hijos 1 y 4
nodo3 = TreeNode(3, izq=nodo1, der=nodo4)

# Hoja 6 (hijo derecho de la raíz, sin hijos)
nodo6 = TreeNode(6)

# Raíz 5 con hijos 3 y 6
raiz = TreeNode(5, izq=nodo3, der=nodo6)

k = 3
n = 0
nodo = raiz
memoria = []

while nodo or memoria:
    while nodo:
        memoria.append(nodo)
        nodo = nodo.izq
    nodo = memoria.pop()
    n += 1
    if n == k:
        print(nodo.val)
        break
    nodo = nodo.der
