nums = [-1,0,1,2,-1,-4]
answer = []
nums.sort()
for i , v in enumerate(nums):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    l , r = i + 1 , len(nums) - 1
    while l < r :
        suma3 = nums[l] + nums[r] + v 
        if suma3 > 0:
            r -= 1
        elif suma3 < 0:
            l += 1
        else:
            answer.append([nums[l] , nums[r] , v])
            r -= 1
            l += 1
            while l < r and nums[l - 1] == nums[l]:
                l += 1
            while l < r and nums[r + 1] == nums[r]:
                r -= 1
print(answer)