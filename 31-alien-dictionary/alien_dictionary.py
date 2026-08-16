words = ["wrt", "wrf", "er", "ett", "rftt"]

lista_ady = {}
for palabra in words:
    for letra in palabra:
        lista_ady[letra] = set()

valido = True

for i in range(len(words) - 1):
    palabra1 = words[i]
    palabra2 = words[i + 1]
    longitud = min(len(palabra1), len(palabra2))

    if palabra1[:longitud] == palabra2[:longitud] and len(palabra1) > len(palabra2):
        valido = False
        break

    for j in range(longitud):
        if palabra1[j] != palabra2[j]:
            lista_ady[palabra1[j]].add(palabra2[j])
            break

visitando = set()
visitados = set()
orden = []

def dfs(letra):
    if letra in visitando:
        return False
    if letra in visitados:
        return True

    visitando.add(letra)

    for vecino in lista_ady[letra]:
        if not dfs(vecino):
            return False

    visitando.remove(letra)
    visitados.add(letra)
    orden.append(letra)
    return True

if valido:
    for letra in lista_ady:
        if not dfs(letra):
            valido = False
            break

if valido:
    print("".join(orden[::-1]))
else:
    print("")
