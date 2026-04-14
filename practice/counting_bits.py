n = 5
dp = [0] * n + 1
resul = [0]
offten = 1

for i in range(1, n +  1):
    if offten * 2 ==  i:
        offten == i
    dp[i] = dp[i - offten] + 1
print(dp)