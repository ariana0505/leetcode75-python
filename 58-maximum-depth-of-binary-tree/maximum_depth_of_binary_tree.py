def maximumDepth(tree):
    if tree is None:
        return 0
    izq = maximumDepth(tree.izq)
    der = maximumDepth(tree.der)
    return 1 + max(izq,der)
