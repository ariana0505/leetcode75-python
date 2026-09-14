intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals.sort(key=lambda x:x[1])
final_ant = intervals[0][1]
eliminar = 0
for inicio, fin in intervals[1:]:
    if final_ant > inicio:
        eliminar += 1

    else:
        final_ant = fin