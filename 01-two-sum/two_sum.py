from typing import List

class Solution:
    def two_sum(self, nums: List[int], target:int) -> List[int]:
        hash_map = {}  # almacena num -> índice

        for i, num in enumerate(nums):
            complement = target - num  # lo que falta para llegar al target 7

            if complement in hash_map:
                # Si ya lo vimos, devolvemos los índices
                return [hash_map[complement], i]

            # Si no, guardamos este número y su índice
            hash_map[num] = i 


if __name__ == "__main__":
   solution = Solution()
   nums = [11,15,2,7]
   target = 9
   result = solution.two_sum(nums, target)
   print(result)