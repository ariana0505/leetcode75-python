
s: str = "abcabcbb"
seen_chars: dict[str, int] = {}
max_substring: int = 0
l: int = 0

for r, char in enumerate(s):
    if char in seen_chars and seen_chars[char] >= l:
        l = seen_chars[char] + 1

    seen_chars[char] = r

    max_substring = max(max_substring, r - l + 1)

print(max_substring)
