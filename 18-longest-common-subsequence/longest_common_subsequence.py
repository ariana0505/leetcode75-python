from functools import lru_cache

text1 = "abcde"
text2 = "ace"


@lru_cache
def lcs(i,j):
    if i == len(text1)  or j ==len(text2):
        return 0
    if text1[i] == text2[j]:
        return 1 +  lcs(i+1,j+1)
    else:
        return  max(lcs(i+ 1,j),lcs(i,j+1))
print(lcs(0,0))