from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"

tengo  = 0
necesito = Counter(t)
faltan  = len(t)
ventana =  {}
resul = ''
resul_len = float('inf')

l = 0
for r in range(len(s)):
    letra = s[r]
    ventana[letra] = ventana.get(letra,0) + 1
    if letra in necesito and necesito[letra] == ventana[letra]:
        faltan  -= 1
    while faltan == 0:
        ventana_len  = r-l+ 1
        if ventana_len < resul_len:
            resul_len  = ventana_len
            resul = s[l:r+1]
        letra_l = s[l]
        ventana[letra_l] -= 1
        if letra_l  in necesito and ventana[letra_l] < necesito[letra_l]:
            faltan +=1
        l +=1
print(resul)