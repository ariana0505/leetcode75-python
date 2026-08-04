n = 5
edges = [[0,1],[1,2],[3,4]]
lista_ady = [[] for _ in range(n)]

for a,b in edges:
    lista_ady[a].append(b)
    lista_ady[b].append(a)

visitados = set()

def dfs(nodo):
    if nodo in visitados:
        return
    visitados.add(nodo)

    for vecino in lista_ady[nodo]:
        dfs(vecino)

contador = 0
for nodo in range(0, n):
    if nodo not in visitados:
        contador += 1
        dfs(nodo)