nums = [100,4,200,1,3,2]
nums_set = set(nums)
mayor_longitud =  0
for num in nums:
    if num - 1 not in nums_set:
        longitud = 1
        while num + longitud in  nums_set:
            longitud += 1
        mayor_longitud = max(longitud,mayor_longitud)
print(mayor_longitud)
