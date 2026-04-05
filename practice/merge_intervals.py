intervals = [[1,3],[2,6],[8,10],[15,18]]
Resul = [intervals[0]]

for i in range(1,len(intervals)):
    if Resul[-1][1] >= intervals[i][0]:
        Resul[-1][1] = max(Resul[-1][1], intervals[i][1])
    else:
        Resul.append(intervals[i])
print(Resul)