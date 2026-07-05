s = "race a car"
l =  0
r =  len(s) - 1

while l<r:
    while l<r and not s[l].isalnum():
        l += 1
    while l<r and not s[r].isalnum():
        r -= 1
    
    if s[l].lower() ==  s[r].lower():
        l +=1
        r  -=  1
    else:
        print(False)
        break
else:
    print(True)