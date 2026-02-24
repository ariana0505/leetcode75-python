# valores de entrada
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

res = []

for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]: # no soplan, esta antes
        res.append(newInterval)
        res.extend(intervals[i:])
        break
    elif newInterval[0] > intervals[i][1]: #no soplan, esta despues
        res.append(intervals[i])
    else: # si soplan
        newInterval = [
            min(newInterval[0], intervals[i][0]),
            max(newInterval[1], intervals[i][1])
        ]
else:
    res.append(newInterval)

print(res)
