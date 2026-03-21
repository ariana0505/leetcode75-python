from typing import List

def findMin(nums: List[int]) -> int:
    left: int = 0
    right: int = len(nums) - 1

    # Already sorted, no rotation
    if nums[left] < nums[right]:
        return nums[left]

    while left < right:
        mid: int = (left + right) // 2

        if nums[mid] > nums[right]:
            # Minimum is in the right half
            left = mid + 1
        else:
            # Minimum is in the left half (including mid)
            right = mid

    return nums[left]


if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))        # 1
    # print(findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    # print(findMin([11, 13, 15, 17]))       # 11
