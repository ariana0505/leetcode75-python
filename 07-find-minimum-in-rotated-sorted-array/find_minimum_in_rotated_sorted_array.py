from typing import List

def findMin(nums: List[int]) -> int:

    left, right = 0, len(nums) - 1
    

    if nums[left] < nums[right]:
        return nums[left]


    while left < right:
        print(f"Left {left}")
        print(f"Right {right}")

        mid = (left + right) // 2
        print(f"MId {mid}")

        if nums[mid] > nums[right]:
            print(f"CASO 1 {nums[mid]} - {nums[right]}")
            left = mid + 1
        else:
            print(f"CASO 2 {nums[mid]} - {nums[right]}")
            right = mid

    return nums[left]


if __name__ == "__main__":
    print(findMin([3, 4, 5, 1, 2]))        # 1
    # print(findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
    # print(findMin([11, 13, 15, 17]))       # 11