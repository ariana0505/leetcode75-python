s = "abcabcbb"
caracteres_vistos = {}
maximo_subtring = 0
l = 0

for r , caracter in enumerate(s):
    if caracter in caracteres_vistos and caracteres_vistos[caracter]>= l:
        l = caracteres_vistos[caracter] + 1
    
    caracteres_vistos[caracter] = r

    maximo_subtring = max(maximo_subtring, r - l + 1)

print(maximo_subtring)