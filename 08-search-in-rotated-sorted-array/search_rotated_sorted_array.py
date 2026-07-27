
nums: list[int] = [4,5,6,7,0,1,2]
target: int = 8
l: int = 0
r: int = len(nums) - 1
while l <= r:
    mid: int = (l + r) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[l] <= nums[mid]:
        # Left half is sorted
        if nums[l] <= target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:
        # Right half is sorted
        if nums[mid] < target <= nums[r]:
            l = mid + 1
        else:
            r = mid - 1
else:
    print(-1)
# <fix>
# The condition was nums[l] < nums[mid], but when l == mid (2-element window)
# nums[l] == nums[mid] and it fell into the wrong branch, returning -1 for valid targets.
# Fixed to nums[l] <= nums[mid].
