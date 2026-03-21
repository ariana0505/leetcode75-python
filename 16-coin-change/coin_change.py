from typing import List

# Available coin denominations
coins: List[int] = [1, 2, 5]

# Target amount to form
amount: int = 11

# dp[i] = minimum number of coins needed to form amount i
dp: List[float] = [float('inf')] * (amount + 1)

# Base case: zero coins needed to form amount 0
dp[0] = 0

for coin in coins:
    for current_amount in range(coin, amount + 1):
        # Take the minimum between not using and using this coin
        dp[current_amount] = min(
            dp[current_amount],
            dp[current_amount - coin] + 1
        )

result: int = dp[amount] if dp[amount] != float('inf') else -1
print("Minimum number of coins:", result)
