n = 11
res = 0
while n != 0:
    res += 1
    n = n & (n - 1)
print(res)