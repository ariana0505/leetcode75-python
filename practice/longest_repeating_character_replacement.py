s = "ABAB"
k = 1
counter =  {}
l = 0
maximo =  0
for r in  range(len(s)):
    counter[s[r]] = counter.get(s[r],0) + 1
    if (r -  l  +  1)  - max(counter.values()) > k:
        counter[s[l]] -= 1
        l += 1
    maximo = max(maximo, r-l+1)
    
print(maximo)