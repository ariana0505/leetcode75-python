n = 5
edges = [[0,1],[1,2],[2,3],[3,4]]
lista_ady = [[] for _ in range(n)]

for a,b in edges:
    lista_ady[a].append(b)
    lista_ady[b].append(a)

visitados = set()

def connected(nodo):
    if nodo in visitados:
        return
    visitados.add(nodo)
    for vecino in lista_ady[nodo]:
        connected(vecino)
componente = 0
for i in range(n):
    if i not in visitados:
        connected(i)
        componente += 1

print(componente)