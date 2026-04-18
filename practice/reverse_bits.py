num = 19321
resul = 0 
for i in range(32):
    bit = (num >> i)  & 1
    resul = resul | ( bit <<   (31 - i))

print(resul)

