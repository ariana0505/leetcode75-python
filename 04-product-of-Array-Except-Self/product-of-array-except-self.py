
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n: int = len(nums)
        answer: list[int] = [1] * n  # final result

        # Step 1: compute prefix products (left to right)
        prefix: int = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Step 2: compute suffix products (right to left)
        suffix: int = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
