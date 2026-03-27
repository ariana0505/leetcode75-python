nums = [100,4,200,1,3,2]
nums_set = set(nums)
mayor = 0
for num in nums_set:
    if num - 1 not in nums_set:
        largo = 1
        while num + largo in nums_set:
            largo += 1
        mayor = max(mayor,largo)

print(mayor)


