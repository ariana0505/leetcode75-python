intervals = [[0,30],[5,10],[15,20]]

inicios= sorted([interval[0] for interval in intervals])
finales= sorted([interval[1] for interval in intervals])

i,j = 0,0

salas_maximas =  0
salas_ahora = 0

while  i  <  len(intervals):
    if  inicios[i] <  finales[j]:
        salas_ahora  +=  1
        i  += 1
        salas_maximas =  max(salas_ahora,salas_maximas)
    else:
        salas_ahora -= 1
        j += 1


print(salas_maximas)