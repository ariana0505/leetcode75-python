

def rob_linear(nums: list[int]) -> int:
    rob1, rob2 = 0, 0
    for money in nums:
        rob1, rob2 = rob2, max(money + rob1, rob2)
    return rob2


def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


if __name__ == "__main__":
    houses = [2, 7, 9, 3, 1]
    assert rob(houses) == 11
    assert rob([5]) == 5
    print(rob(houses))
