
# Determine whether s can be segmented into words from the dictionary
s: str = "leetcode"
wordDict: list[str] = ["leet", "code"]

dp: list[bool] = [False] * (len(s) + 1)
dp[len(s)] = True

for i in range(len(s) - 1, -1, -1):
    for word in wordDict:
        if (i + len(word) <= len(s)) and (s[i: i + len(word)] == word):
            dp[i] = dp[i + len(word)]
        if dp[i]:
            break

print(dp[0])
