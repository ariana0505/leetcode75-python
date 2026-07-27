
# Input values
intervals: list[list[int]] = [[1, 3], [6, 9]]
newInterval: list[int] = [2, 5]

res: list[list[int]] = []

for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:  # No overlap, new interval comes before
        res.append(newInterval)
        res.extend(intervals[i:])
        break
    elif newInterval[0] > intervals[i][1]:  # No overlap, new interval comes after
        res.append(intervals[i])
    else:  # Overlapping intervals, merge them
        newInterval = [
            min(newInterval[0], intervals[i][0]),
            max(newInterval[1], intervals[i][1])
        ]
else:
    res.append(newInterval)

print(res)
