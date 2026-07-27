
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        hash_map: dict[int, int] = {}  # stores num -> index

        for i, num in enumerate(nums):
            complement: int = target - num  # value needed to reach target

            if complement in hash_map:
                # Already seen the complement, return both indices
                return [hash_map[complement], i]

            # Otherwise, store this number and its index
            hash_map[num] = i


if __name__ == "__main__":
   solution = Solution()
   nums = [11,15,2,7]
   target = 9
   result = solution.two_sum(nums, target)
   print(result)
