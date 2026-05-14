s = "babad"
resol =  ""
resol_t  =  0

for i in range(len(s)):
    l,r=  i,i
    while l >= 0 and r < len(s)  and s[l]  == s[r]:
        if r - l  +  1  > resol_t:
            resol = s[l:r+1]
            resol_t = r - l  +  1
        l -= 1
        r += 1
    l,r = i,i+1
    while l >= 0 and r < len(s)  and s[l]  == s[r]:
        if r - l  +  1  > resol_t:
            resol = s[l:r+1]
            resol_t = r - l  +  1
        l -= 1
        r += 1

print(resol)