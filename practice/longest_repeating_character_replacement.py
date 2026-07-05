s = "ABABB"
k = 1

contador  = {}
maximo = 0
l = 0

for  r in  range(len(s)):
    contador[s[r]] = contador.get(s[r],0)+1
    if (r-l + 1) - max(contador.values()) > k:
        contador[s[l]] -= 1
        l += 1
    
    maximo  =  max(maximo,  r-l+1)
print(maximo)