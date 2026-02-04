from collections import Counter

s = "antena"
t = "atenea"
if Counter(s) == Counter(t):
    print(True)
else:
    print(False)