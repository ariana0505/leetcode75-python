intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals.sort(key = lambda x: x[1])
final_anterior = intervals[0][1]

eliminados = 0

for inicio, fin in intervals[1:]:
    if inicio < final_anterior:
        eliminados += 1
    else:
        final_anterior = fin

print(eliminados)
    
