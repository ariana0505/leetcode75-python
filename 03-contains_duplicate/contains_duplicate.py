from typing import List

# my way of solving
def containsDuplicateWithHashMap(nums: List[int]) -> bool:
    hash_map = {}
    for i, v in enumerate(nums):
        if v in hash_map:
            return True
        hash_map[v] = i
    return False

#the most optimal and fastest way
def containsDuplicateWithSet(nums: List[int]) -> bool:
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False
