n = 5
edges = [[0,1],[0,2],[0,3],[1,4]]
lista_ady =[[] for _ in range(n)]

for a,b in edges:
    lista_ady[a].append(b)
    lista_ady[b].append(a)

visitados = set()

def valid(nodo):
    if nodo in visitados:
        return 
    visitados.add(nodo)
    for vecino in lista_ady[nodo]:
        valid(vecino)

if len(edges) != (n-1):
    print(False)
else:
    valid(0)
    print(len(visitados) == n)