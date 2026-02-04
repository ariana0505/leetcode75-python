nums = [9,6,4,2,3,5,7,0,1]
ans = 0
for i in range(len(nums)+ 1):
    ans ^= i

for i in nums:
    ans ^= i

print(ans)