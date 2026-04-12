nums = [3,2,1,1,4]   
meta = len(nums)  - 1
for i in range(len(nums) -2,-1,-1):
    if nums[i] + i >= meta:
        meta = i

if meta == 0:
    print(True)
else:
    print(False)