from typing import Dict, List

k: int = 2  # Number of most frequent elements to find
nums: List[int] = [1, 1, 1, 2, 2, 3]
freq: List[List[int]] = [[] for i in range(len(nums) + 1)]
count: Dict[int, int] = {}

for num in nums:
    count[num] = 1 + count.get(num, 0)

# Apply Bucket Sort
for n, c in count.items():  # (1,3), (2,2), (3,1) -> number, frequency
    freq[c].append(n)  # freq = [[], [3], [2], [1], [], [], []]

res: List[int] = []
for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)
# <fixed>
# Used count[nums] instead of count[num] (the entire list instead of the loop variable).
# This caused TypeError: unhashable type: 'list'.
