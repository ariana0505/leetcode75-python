nums = [0,3,7,2,5,8,4,6,0,1]

nums_set = set(nums)
mayor_largo = 0

for num in nums_set:
    if  num - 1 not in nums:
        largo = 1
        while num + largo in  nums_set:
            largo += 1
        mayor_largo = max(largo,mayor_largo)

print(mayor_largo)