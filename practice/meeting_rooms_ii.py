intervals = [[7,10],[2,4]]

inicios = sorted([interval[0]  for  interval in intervals])
finales = sorted([interval[1]  for  interval in intervals])

salas_ahora =  0
salas_maximo  = 0

i,f =0,0

while i < len(intervals):
    if inicios[i] < finales[f]:
        salas_ahora += 1
        i += 1
        salas_maximo = max(salas_maximo,salas_ahora)
    else:
        f += 1
        salas_ahora -=  1

print(salas_maximo)
