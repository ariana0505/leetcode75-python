# valores de entrada
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

res = []

for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:
        res.append(newInterval)
        res.extend(intervals[i:])
        break
    elif newInterval[0] > intervals[i][1]:
        res.append(intervals[i])
    else:
        newInterval = [
            min(newInterval[0], intervals[i][0]),
            max(newInterval[1], intervals[i][1])
        ]
else:
    res.append(newInterval)

print(res)
