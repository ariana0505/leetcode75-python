nums = [1,3,7,9,12,14]
l ,r = 0 , len(nums) - 1
target = 26
while l < r :
    suma = nums[l] + nums[r]
    if suma == target:
        print([l + 1 , r + 1])
        break
    if suma < target:
        l += 1
    else:
        r -= 1
# <arreglado>
# Faltaba un break despues de encontrar el resultado, lo que causaba que el loop
# siguiera iterando innecesariamente y pudiera imprimir resultados incorrectos.
#
# Missing a break after finding the result, causing the loop to keep iterating
# unnecessarily and potentially printing incorrect results.