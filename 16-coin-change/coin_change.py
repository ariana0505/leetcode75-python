coins = [1,2,5]
amount = 11

dp =[float('inf') ] * (amount + 1)
dp[0] = 0

for coin in coins:
    for amount_current in range(coin,  amount + 1):
        dp[amount_current] = min(dp[amount_current], dp[amount_current - coin] + 1)

if  dp[amount] == float('inf'):
    print( -1)
else:
    print(dp[amount])
