n = 2147483644
res = 0
for i in range(32):
    bit = (n >> i) & 1
    res = res | (bit << (31 - i))
print(res)