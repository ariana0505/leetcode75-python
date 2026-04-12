letras = "abcdabcbb"
l = 0
resul = ""
maxi = 0
for r in range(len(letras)):
    while letras[r] in resul:
        l += 1
        resul = letras[l:r]
    resul = letras[l:r+1]
    maxi = max(len(resul), maxi)

print(maxi)