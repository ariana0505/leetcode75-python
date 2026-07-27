
# Hash map approach
def containsDuplicateWithHashMap(nums: list[int]) -> bool:
    hash_map: dict[int, int] = {}
    for i, v in enumerate(nums):
        if v in hash_map:
            return True
        hash_map[v] = i
    return False

# Optimal approach using a set (faster lookups, no index storage)
def containsDuplicateWithSet(nums: list[int]) -> bool:
    hashset: set[int] = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
