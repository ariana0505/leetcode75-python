a: int
b: int
a, b = 3, 5
mask: int = 0xFFFFFFFF
while (b & mask) != 0:
    tmp: int = (a & b) << 1
    a = a ^ b
    b = tmp
if a > 0x7FFFFFFF:
    a = ~(a ^ mask)
print(a)
# <fixed>
# With negative numbers this entered an infinite loop because Python has arbitrary-precision
# integers and negative bits grow without bound. A 32-bit mask (0xFFFFFFFF) was added
# to simulate 32-bit integer overflow.
