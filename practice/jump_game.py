nums = [2,3,1,0,4]
meta = len(nums)- 1
for i in range(len(nums) - 2, -1, -1):
    if nums[i] + i >= meta:
        meta = i
    
print(meta == 0)