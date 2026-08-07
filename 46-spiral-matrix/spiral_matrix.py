matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = []

izq , der = 0 , len(matrix[0]) - 1

top , bottom = 0, len(matrix) - 1

while top <= bottom and izq <= der:
    # top representa la columna que a de recorrer
    # sus topes es izq y der + 1
    for col in range(izq,der +1):
        result.append(matrix[top][col])
    top += 1

    # fila representa bajar de top a bottom
    for fila in range(top, bottom + 1):
        result.append(matrix[fila][der])

    der -= 1

    if top <= bottom:
        # recorre la fila bottom de derecha a izquierda
        for col in range(der, izq - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1

    if izq <= der:
        # sube de bottom a top por la columna izq
        for fila in range(bottom, top - 1, -1):
            result.append(matrix[fila][izq])
        izq += 1

print(result)