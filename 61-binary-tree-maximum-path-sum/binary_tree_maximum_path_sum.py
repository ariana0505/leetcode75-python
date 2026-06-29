class TreeNode:
    def  __init__(self,valor,izq  = None, der  = None):
        self.valor = valor
        self.izq  = izq
        self.der =  der


mejor  =  float("-inf")
def dfs(node:TreeNode):
    global  mejor
    if not node:
        return 0
    izq  = max(dfs(node.izq),0)
    der = max(dfs(node.der),0)
    mejor =max(mejor,node.valor + der +  izq )
    return node.valor +  max(izq,der)



if __name__ == "__main__":
    # Ejemplo: [-10, 9, 20, null, null, 15, 7]
    #       -10
    #       /  \
    #      9    20
    #          /  \
    #         15    7
    raiz = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    dfs(raiz)
    print(mejor)  # 42