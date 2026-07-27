

def rob_linear(nums: list[int]) -> int:
    # House Robber 1: linear algorithm
    rob1, rob2 = 0, 0
    for money in nums:
        temp: int = max(money + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


houses: list[int] = [2, 7, 9, 3, 1]

# Break the circle into two lines
# Line 1: houses[0 ... n-2] (include first, exclude last)
# Line 2: houses[1 ... n-1] (exclude first, include last)

result: int = max(rob_linear(houses[:-1]), rob_linear(houses[1:]))
print(result)
