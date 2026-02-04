n = 5
dp = [0] * (n + 1)
op = 1
for i in range(1 , n + 1):
    if op * 2 == i:
        op = i
    dp[i] = 1 + dp[i - op]
print(dp)