nums = [1,2,3,1]
def rob(nums):
    rob1,  rob2 = 0,0
    for num  in nums:
        temp  = max(rob1 + num,rob2)
        rob1   = rob2
        rob2 = temp
    
    return rob2

print(max(rob(nums[1:]),rob(nums[:-1])))