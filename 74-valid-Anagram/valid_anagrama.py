from collections import Counter

s: str = "antena"
t: str = "atenea"
if Counter(s) == Counter(t):
    print(True)
else:
    print(False)
