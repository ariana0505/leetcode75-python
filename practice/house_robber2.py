nums = [1,2,3,1]

def rob(nums):
    rob1 = 0
    rob2 = 0

    for num in nums:
        temp = max(num + rob1,  rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

if len(nums) == 1:
    print(nums[0])
else:
    print(max(rob(nums[:-1]),rob(nums[1:])))