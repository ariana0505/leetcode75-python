nums = [-1,0,3,5,9,12]
target = 3

izq, der = 0 , len(nums) - 1
while izq <= der:
    mid = (izq + der) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid]> target:
        der = mid - 1
    else:
        izq = mid + 1
else:
    print(-1)