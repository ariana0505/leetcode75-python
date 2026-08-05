n = 5
edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

lista_ady = [[] for _ in range(n)]

for a,b in edges:
    lista_ady[a].append(b)
    lista_ady[b].append(a)

visitados = []

def valid(nodo):
    if nodo in visitados:
        return
    visitados.append(nodo)
    for vecino in lista_ady[nodo]:
        valid(vecino)

if len(edges) != (n - 1):
    print(False)
else:
    valid(0)
    print(n == len(visitados))

