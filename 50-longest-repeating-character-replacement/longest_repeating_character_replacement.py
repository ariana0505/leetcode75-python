s = "AABABBA"
k = 1

contador = {}
resul = 0


l =  0
for r in range(len(s)):
    contador[s[r]] = contador.get(s[r],0) + 1
    while (r  - l + 1) - max(contador.values()) > k: # sobrepasamos los cambios permitidos?
        contador[s[l]] -= 1 # si  olvidate de este valor
        l += 1 # avanza para que  la ventana  vuelva a ser valida
    resul = max(resul, r-l+1)

print(resul)