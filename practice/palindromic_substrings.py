s =  "babab"


resol_t = 0

for i in range(len(s)):
    l,r=i,i
    # impares
    while l >= 0 and r < len(s) and s[l]  == s[r]:
           
        resol_t += 1
        l-=1
        r+=1
    # pares
    l,r=i,i+1
    while l >= 0 and r < len(s) and s[l]  == s[r]:
            
        resol_t  +=1
        l-=1
        r+=1

print(resol_t)