import bisect
from typing import List

# Find the length of the longest increasing subsequence using patience sorting
nums: List[int] = [0, 1, 0, 3, 2, 3]

tails: List[int] = []

for num in nums:
    # Find the insertion point for num in the sorted tails array
    pos: int = bisect.bisect_left(tails, num)

    if pos == len(tails):
        tails.append(num)
    else:
        tails[pos] = num

print(len(tails))
