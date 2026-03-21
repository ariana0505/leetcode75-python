from typing import List

nums: List[int] = [-1,0,1,2,-1,-4]
answer: List[List[int]] = []
nums.sort()
for i, v in enumerate(nums):
    # Skip duplicate values for the first element
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l: int = i + 1
    r: int = len(nums) - 1
    while l < r:
        three_sum: int = nums[l] + nums[r] + v
        if three_sum > 0:
            r -= 1
        elif three_sum < 0:
            l += 1
        else:
            answer.append([nums[l], nums[r], v])
            r -= 1
            l += 1
            # Skip duplicates for left and right pointers
            while l < r and nums[l - 1] == nums[l]:
                l += 1
            while l < r and nums[r + 1] == nums[r]:
                r -= 1
print(answer)
