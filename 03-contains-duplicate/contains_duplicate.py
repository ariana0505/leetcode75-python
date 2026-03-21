from typing import Dict, List

# Hash map approach
def containsDuplicateWithHashMap(nums: List[int]) -> bool:
    hash_map: Dict[int, int] = {}
    for i, v in enumerate(nums):
        if v in hash_map:
            return True
        hash_map[v] = i
    return False

# Optimal approach using a set (faster lookups, no index storage)
def containsDuplicateWithSet(nums: List[int]) -> bool:
    hashset: set[int] = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
