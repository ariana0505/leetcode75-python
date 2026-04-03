intervals = [[7,10],[2,4]]


intervals.sort()


for i in range(len(intervals) - 1):
    if intervals[i][1] > intervals[i + 1][0]:
        print(False)
        break
else:
    print(True)
