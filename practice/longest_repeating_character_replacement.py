s = "AABABBA"
k = 1
contador = {}
resul = 0
l = 0
for r in range(len(s)):
    contador[s[r]] =contador.get(s[r],0) +  1
    while  (r - l + 1 ) - max(contador.values()) > k:
        contador[s[l]] -= 1
        l +=  1
    resul = max(resul,  r - l +  1)

print(resul)