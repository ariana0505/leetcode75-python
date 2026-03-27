intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Sort intervals by start time
intervals.sort()

# Start with the first interval
result = [intervals[0]]

for start, end in intervals[1:]:
    # If current interval overlaps with the last merged one
    if result[-1][1] >= start:
        # Extend the end to the max of both
        result[-1][1] = max(result[-1][1], end)
    else:
        # No overlap, add as new interval
        result.append([start, end])

print(result)
