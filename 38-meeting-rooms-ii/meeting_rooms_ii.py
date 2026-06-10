intervalos = [[7,10],[2,4]]

inicios = sorted([i[0] for i in intervalos])

finales = sorted([i[1] for i in intervalos])

i =  0
f = 0
salas_max_alcanzado  = 0 
salas_max_ahora = 0

while i < len(intervalos):
    if inicios[i] < finales[f]:
        salas_max_ahora +=1
        salas_max_alcanzado = max(salas_max_alcanzado, salas_max_ahora)
        i+=1
    else:
        f += 1
        salas_max_ahora -= 1

print(salas_max_alcanzado)