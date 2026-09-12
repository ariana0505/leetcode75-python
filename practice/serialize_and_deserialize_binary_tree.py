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

def serializar(nodo:TreeNode,):
    # 1. Guardamos aquí los valores encontrados durante el recorrido.
    lista = []
    def recorrer(nodo):
        # 2. Marcamos los hijos vacíos para conservar la forma del árbol.
        if nodo is None:
            lista.append("N")
            return 
        # 3. Visitamos el nodo antes de recorrer sus hijos (preorden).
        lista.append(str(nodo.val))

        # 4. Procesamos primero la rama izquierda y luego la derecha.
        recorrer(nodo.left)
        recorrer(nodo.right)
    
    recorrer(nodo)
    # 5. Unimos las marcas y los valores en una sola cadena.
    return ",".join(lista)

def deserializacion(texto:str):
    # 1. Convertimos la cadena en un iterador para consumirla en orden.
    valores = iter(texto.split(","))

    def recorrer():
        # 2. Cada llamada toma el siguiente elemento del recorrido preorden.
        valor = next(valores)

        # 3. Una marca representa la ausencia de un nodo.
        if valor == "N":
            return None

        # 4. Creamos el nodo y reconstruimos recursivamente sus dos ramas.
        nodo = TreeNode(int(valor))
        nodo.left = recorrer()
        nodo.right = recorrer()
        return nodo
    # 5. La primera llamada reconstruye el árbol desde la raíz.
    return recorrer()
