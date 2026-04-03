intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
resultado = [intervals[0]]

for i in range(1,len(intervals)):
    if resultado[-1][1] >= intervals[i][0]:
        resultado[-1][1] = max(resultado[-1][1], intervals[i][1])
    else:
        resultado.append(intervals[i])

print(resultado)

