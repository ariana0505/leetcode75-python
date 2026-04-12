n = 0b11111111111111111111111111111101

resul  = 0
for i in range(32):
    bit = (n >>i) & 1
    resul =  resul | bit <<  (31 - i)

print(resul)