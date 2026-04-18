from  collections import Counter

s = "anagram"
t = "nagaram"

if Counter(s) == Counter(t):
    print(True)
else:
    print(False)