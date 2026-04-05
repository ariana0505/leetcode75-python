nums = [0,3,7,2,5,8,4,6,0,1]
nums_set = set(nums)
longest = 0

for num in nums_set:
    if num - 1 not in nums_set:
        long = 1
        while num + long in nums_set:
            long += 1
        longest = max(long,longest)

print(longest)