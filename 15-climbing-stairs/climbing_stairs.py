# Climbing stairs: count distinct ways to reach step n (Fibonacci approach)
n: int = 8
one: int = 1
two: int = 1

# Iterate n times, shifting the two-variable window forward
for i in range(n):
    temp: int = one
    one = one + two
    two = temp

print(temp)
