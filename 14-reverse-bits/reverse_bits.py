# Reverse the bits of a 32-bit unsigned integer
n: int = 2147483644
res: int = 0
for i in range(32):
    bit: int = (n >> i) & 1
    res = res | (bit << (31 - i))
print(res)
