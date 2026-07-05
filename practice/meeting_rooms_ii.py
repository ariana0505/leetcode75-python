intervals = [[0,30],[5,10],[15,20]]

inicios = sorted([interval[0]  for interval  in intervals])
finales = sorted([interval[1]  for interval  in intervals])

salas_ahora = 0
salas_maximas = 0

i,f =   0,0

while  i < len(intervals):
    if inicios[i] < finales[f]:
        i += 1
        salas_ahora += 1
        salas_maximas   =  max(salas_maximas,salas_ahora)
    else:
        f += 1
        salas_ahora -= 1

print(salas_maximas)