from typing import List

# Count the number of 1-bits for every number from 0 to n
n: int = 5
dp: List[int] = [0] * (n + 1)
offset: int = 1
for i in range(1, n + 1):
    if offset * 2 == i:
        offset = i
    dp[i] = 1 + dp[i - offset]
print(dp)
