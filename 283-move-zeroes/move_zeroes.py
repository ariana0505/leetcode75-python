nums = [0,1,0,3,12]

izq = 0 

for der in range(len(nums)):
    if nums[der] != 0:
        nums[izq],nums[der] = nums[der],nums[izq]
        izq += 1

print(nums)