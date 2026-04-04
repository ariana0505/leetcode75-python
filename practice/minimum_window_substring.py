from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"

necesito = Counter(t)       # cuenta cuántas de cada letra necesitamos de t
faltan = len(necesito)      # cuántas letras únicas aún faltan por cumplir
ventana = {}                # cuenta las letras dentro de la ventana actual
l = 0                       # puntero izquierdo de la ventana
resultado = ""              # el substring mínimo encontrado
min_long = float("inf")    # largo del substring mínimo (empieza en infinito)


for r in range(len(s)):
    char = s[r]
    ventana[char] = ventana.get(char,0) + 1
    if char in necesito and ventana[char] == necesito[char]:
        faltan -= 1
    while faltan   == 0:
        largo =  r - l + 1
        if largo  < min_long:
            min_long = largo
            resultado = s[l:r + 1]
        letra_l = s[l]
        ventana[letra_l] -= 1

        if letra_l  in necesito and ventana[letra_l] < necesito[letra_l]:
            faltan +=  1
        l +=1

print(resultado)