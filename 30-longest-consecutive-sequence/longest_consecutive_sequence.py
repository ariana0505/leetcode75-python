
# Given an unsorted array of integers, return the length of the longest consecutive sequence.
# Must run in O(n) time.

nums = [100, 4, 200, 1, 3, 2]

# Create a set for O(1) lookups
num_set = set(nums)

longest = 0

for num in num_set:
    # Only start counting if num is the beginning of a sequence
    if num - 1 not in num_set:
        length = 1
        # Count consecutive numbers forward
        while num + length in num_set:
            length += 1
        longest = max(longest, length)

print(longest)  # 4