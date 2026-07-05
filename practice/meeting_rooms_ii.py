intervals = [[7,10],[2,4]]

inicios =  sorted([interval[0] for interval in intervals])
finales =  sorted([interval[1] for interval in intervals])
i,f= 0,0
salas_ahora = 0
salas_maximas = 0

while i <  len(intervals):
    if inicios[i]  <  finales[f]:
        salas_ahora += 1
        i += 1
        salas_maximas =  max(salas_maximas,salas_ahora)
    else:
        salas_ahora  -= 1
        f+= 1
    
print(salas_maximas)