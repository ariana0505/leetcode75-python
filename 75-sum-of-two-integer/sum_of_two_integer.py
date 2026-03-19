a , b = 3 ,5
mask = 0xFFFFFFFF
while (b & mask) != 0:
        tmp = (a & b) << 1
        a = a ^ b
        b = tmp
if a > 0x7FFFFFFF:
    a = ~(a ^ mask)
print(a)
# <arreglado>
# Con numeros negativos entraba en loop infinito porque Python tiene enteros de precision
# arbitraria y los bits negativos crecen sin limite. Se agrego una mascara de 32 bits
# (0xFFFFFFFF) para simular el overflow de enteros de 32 bits.
#
# With negative numbers it entered an infinite loop because Python has arbitrary precision
# integers and negative bits grow without bound. Added a 32-bit mask (0xFFFFFFFF)
# to simulate 32-bit integer overflow.
