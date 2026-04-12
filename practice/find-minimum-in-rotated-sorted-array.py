nums = [3,4,5]
resul = nums[0]
l = 0
r = len(nums) - 1
while l <= r:
    mid =(l +r)// 2
    resul = min (nums[mid],resul )
    if nums[l]  <= nums[r]:
        print(nums[l])
        break
    if nums[mid] >= nums[l]:
        l = mid  + 1
    else:
        r = mid - 1