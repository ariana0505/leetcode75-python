from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Two pointers: insert_pos marks where the next non-zero goes
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        for i in range(insert_pos, len(nums)):
            nums[i] = 0


if __name__ == "__main__":
    sol = Solution()

    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print(nums1)

    nums2 = [0]
    sol.moveZeroes(nums2)
    print(nums2)

    nums3 = [1, 2, 3]
    sol.moveZeroes(nums3)
    print(nums3)

    nums4 = [0, 0, 0, 1]
    sol.moveZeroes(nums4)
    print(nums4)

    nums5 = [4, 0, 5, 0, 6]
    sol.moveZeroes(nums5)
    print(nums5)

    nums6 = [1]
    sol.moveZeroes(nums6)
    print(nums6)

    nums7 = [0, 0]
    sol.moveZeroes(nums7)
    print(nums7)
