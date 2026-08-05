n = 5
edges = [[0,1],[1,2],[3,4]]

lista_ady = [ [] for _ in range(n) ]

for a,b in edges:
    lista_ady[a].append(b)
    lista_ady[b].append(a)

visitados = []

def connected(nodo):
    if nodo in visitados :
        return

    visitados.append(nodo)

    for vecino in lista_ady[nodo]:
        connected(vecino)

conenxos = 0 

for i in range(n):
    if i not in visitados:
        connected(i)
        conenxos += 1

print(conenxos)