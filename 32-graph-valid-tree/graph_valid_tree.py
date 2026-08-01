n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
visitados = set()
list_ady = [[] for _ in range(n)]
for a,b in edges:
    list_ady[a].append(b)
    list_ady[b].append(a)

def graphValidTree(nodo):
    if nodo in visitados:
        return
    visitados.add(nodo)
    for vecino in list_ady[nodo]:
        graphValidTree(vecino)

if len(edges) != (n - 1):
    print(False)
else:
    graphValidTree(0)
    print(len(visitados) == n)
