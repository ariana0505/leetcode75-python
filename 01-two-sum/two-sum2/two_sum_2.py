nums = [1,3,7,9,12,14]
l ,r = 0 , len(nums) - 1
target = 26
while l < r :
    suma = nums[l] + nums[r]
    if suma == target:
        print([l + 1 , r + 1])
        
    if suma < target:
        l += 1
    else:
        r -= 1