nums = [-1,0,3,5,9,12]
target = 9
izq, der = 0, len(nums) - 1
while izq <= der:
    mid = (izq + der) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] < target:
        izq = mid + 1
    else:
        der = mid - 1
else:
    print(-1)