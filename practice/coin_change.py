coins = [1,2,5] 
amount = 11 

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for  coin in coins:
    for amoun_current in  range(coin, amount + 1):
        dp[amoun_current] =  min(dp[amoun_current], dp[amoun_current  - coin]  +   1)
if dp[amount] == float('inf'):
    print(-1)
else :
    print(dp[amount])