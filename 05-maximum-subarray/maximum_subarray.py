
nums: list[int] = [-2,1,-3,4,-1,2,1,-5,4]
max_sum: int = nums[0]
current_sum: int = nums[0]

for i in range(1, len(nums)):
    current_sum = max(nums[i], current_sum + nums[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
# <fix>
# The old code reset current_sum to 0 when negative, so for all-negative arrays
# (e.g. [-3,-2,-5,-1]) it returned 0 instead of the largest negative (-1).
# Fixed using Kadane's algorithm: current_sum = max(nums[i], current_sum + nums[i])
