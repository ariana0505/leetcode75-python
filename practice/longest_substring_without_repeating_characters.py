s = "abcabcbb"
l = 0
diccionario = {}
maxsun = 0
for r in range(len(s)):
    if s[r] in diccionario and diccionario[s[r]] >= l:
        l = diccionario[s[r]] + 1
    diccionario[s[r]] = r
    maxsun = max(maxsun, r - l + 1)

print(maxsun)
