s  =  "A man, a plan, a canal: Panama"

r,l = 0, len(s) -  1

while  r < l:
     # saltar basura por la izquierda
    while r < l and not s[r].isalnum():
        r += 1
    # saltar basura por la derecha
    while r < l and not s[l].isalnum():
        l -= 1
    # aquí s[r] y s[l] YA son válidos 

    if s[r].lower()  ==  s[l].lower():
        r+=1
        l -=1
    else:
        print(False)
        break
else:
    print(True)