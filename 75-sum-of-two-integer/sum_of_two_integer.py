a , b = 3 ,5
while b != 0:
        tmp = (a & b) << 1
        a = a ^ b
        b = tmp
print(a)
