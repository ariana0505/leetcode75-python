intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()
result = [intervals[0]]

for start, end in intervals[1:]:
    if result[-1][1] >= start:
        result[-1][1] = max(result[-1][1], end)
    else:
        result.append([start, end])

print(result)
