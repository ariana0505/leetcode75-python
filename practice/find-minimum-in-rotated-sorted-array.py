nums = [3,4,5,1,2]

l = 0
r = len(nums) - 1

while l<r:

    mid = (l + r )//2
    if nums[mid] < nums[r]:
        l = mid + 1
    else:
        r = mid
print(nums[mid])