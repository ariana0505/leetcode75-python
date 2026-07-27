
nums: list[int] = [1,3,7,9,12,14]
l: int
r: int
l, r = 0, len(nums) - 1
target: int = 26
while l < r:
    total: int = nums[l] + nums[r]
    if total == target:
        print([l + 1, r + 1])
        break
    if total < target:
        l += 1
    else:
        r -= 1
# <fix>
# A break was missing after finding the result, which caused the loop to keep
# iterating unnecessarily and potentially printing incorrect results.
