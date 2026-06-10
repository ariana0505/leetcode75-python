s = "A man, a plan, a canal: Panama"
limpio = ""
for c in s.lower():
    if c.isalnum(): # es letra?
        limpio += c
    
# vemos  si   es  palindrome
l = 0
r = len(limpio) - 1

while l<=r:
    if limpio[l] ==  limpio[r]:
        l  += 1
        r -=1
    else:
        print(False)
        break
else:
    print(True)