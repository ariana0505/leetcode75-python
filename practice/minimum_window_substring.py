from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"

letras_t =  Counter(t)

have = 0 # letras que ya tengo
need = len(letras_t) # letras q necesito 
window = {} # diccionario de  las letrras q este en tu resultado
resul = "" # mejor de los string
resul_len = float("inf") 
l = 0
for r in range(len(s)):
    letra = s[r]
    window[letra] = window.get(letra,0) + 1

    if letra in letras_t and window[letra] == letras_t[letra]:
        have += 1
    while have == need:
        if r - l + 1 < resul_len:
            resul_len = r - l + 1
            resul = s[l:r + 1]
        
        window[s[l]] -= 1
        if s[l] in letras_t and window[s[l]] < letras_t[s[l]]:
            have -= 1
        l += 1

print(resul)