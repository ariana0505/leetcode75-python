nums = [4,5,6,7,0,1,2]
target = 8
l , r = 0 , len(nums) - 1
while l <= r :
    mid = (l + r) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[l] < nums[mid]:
        if nums[l] <= target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:
        if nums[mid] < target <= nums[r]:
            l = mid + 1
        else:
            r = mid - 1
else:
    print(-1)