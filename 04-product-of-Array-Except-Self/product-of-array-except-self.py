from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n  # resultado final

        # Paso 1️⃣: calcular productos prefix (izquierda → derecha)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Paso 2️⃣: calcular productos suffix (derecha → izquierda)
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer