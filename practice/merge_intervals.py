
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
resul = [intervals[0]]
for i in range(1,len(intervals)):
    if intervals[i][0] <= resul[-1][1]:
        resul[-1][1] = max(intervals[i][1],resul[-1][1])
    else:
        resul.append(intervals[i])
print(resul)