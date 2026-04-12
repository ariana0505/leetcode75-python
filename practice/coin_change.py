coins = [1,2,5]
amount = 11

dp = [float('inf')]  * (amount + 1)
dp[0]  = 0

for coin in  coins :
    for amout_currect in  range(coin, amount + 1):
        dp[amout_currect] = min(dp[amout_currect], (dp[amout_currect - coin]) + 1)


if dp[amount] ==  float('inf'):
    print(-1)
else:
    print(dp[amount])
