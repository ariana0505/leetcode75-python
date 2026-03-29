from collections import Counter
s = "ADOBECODEBANC"
t = "ABC"

letras_t =  Counter(t)

have = 0 # letras que ya tengo
need = len(letras_t) # letras q necesito
window = {}
result = ""
result_len = float("inf")
l = 0

for r in range(len(s)):
    char = s[r]
    window[char] = window.get(char, 0) + 1

    if char in letras_t and window[char] == letras_t[char]:
        have += 1

    while have == need:
        if (r - l + 1) < result_len:
            result_len = r - l + 1
            result = s[l:r + 1]

        window[s[l]] -= 1
        if s[l] in letras_t and window[s[l]] < letras_t[s[l]]:
            have -= 1
        l += 1

print(result)
