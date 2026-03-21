from typing import List

# Find the missing number in [0..n] using XOR
nums: List[int] = [9, 6, 4, 2, 3, 5, 7, 0, 1]
ans: int = 0

# XOR all indices from 0 to n
for i in range(len(nums) + 1):
    ans ^= i

# XOR all values in nums; the remaining value is the missing number
for i in nums:
    ans ^= i

print(ans)
