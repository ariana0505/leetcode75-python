nums = [2,3,2]

def rob(nums):
    rob1 = 0
    rob2 = 0

    for n  in nums:
        temp =  max(n + rob1,rob2)
        rob1 = rob2
        rob2 = temp
    return  rob2
print(max(rob(nums[:-1]), rob(nums[1:])))