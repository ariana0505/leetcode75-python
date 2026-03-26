# Minimum Window Substring
# Find the smallest substring of s that contains all characters of t (including duplicates).
# Uses sliding window technique with two pointers.

from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"

# Count how many of each character we need from t
need = Counter(t)
# How many unique characters we still need to satisfy
remaining = len(need)

left = 0
result = ""
result_len = float("inf")

# Track how many of each character we have in our current window
window = {}

for right in range(len(s)):
    char = s[right]
    window[char] = window.get(char, 0) + 1

    # If this character now meets the required count, one less to satisfy
    if char in need and window[char] == need[char]:
        remaining -= 1

    # When all characters are satisfied, shrink from the left
    while remaining == 0:
        # Update result if this window is smaller
        window_len = right - left + 1
        if window_len < result_len:
            result_len = window_len
            result = s[left:right + 1]

        # Remove left character from window and move left pointer
        left_char = s[left]
        window[left_char] -= 1
        if left_char in need and window[left_char] < need[left_char]:
            remaining += 1
        left += 1

print(result)  # BANC
