# Count the number of set bits (1-bits) using Brian Kernighan's algorithm
n: int = 11
res: int = 0
while n != 0:
    res += 1
    # Clear the lowest set bit
    n = n & (n - 1)
print(res)
