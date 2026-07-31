n = 5
edges = [[0,1],[1,2],[3,4]]

lista_ady = [[] for _ in range(n)]
for a, b in edges:
    lista_ady[a].append(b)
    lista_ady[b].append(a)

componentes = 0
visitados = set()
def dfs(nodo):
    visitados.add(nodo)
    for vecino in lista_ady[nodo]:
        if vecino not in visitados:
            dfs(vecino)

for nodo in range(n):
    if nodo not in visitados:
        componentes += 1
        dfs(nodo)

print(componentes)