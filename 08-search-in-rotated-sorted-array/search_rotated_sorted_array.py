nums = [4,5,6,7,0,1,2]
target = 8
l , r = 0 , len(nums) - 1
while l <= r :
    mid = (l + r) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[l] <= nums[mid]:
        if nums[l] <= target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    else:
        if nums[mid] < target <= nums[r]:
            l = mid + 1
        else:
            r = mid - 1
else:
    print(-1)
# <arreglado>
# La condicion era nums[l] < nums[mid], pero cuando l == mid (ventana de 2 elementos)
# nums[l] == nums[mid] y caia en la rama incorrecta, devolviendo -1 para targets validos.
# Se corrigio a nums[l] <= nums[mid].
#
# The condition was nums[l] < nums[mid], but when l == mid (2-element window)
# nums[l] == nums[mid] and it fell into the wrong branch, returning -1 for valid targets.
# Fixed to nums[l] <= nums[mid].