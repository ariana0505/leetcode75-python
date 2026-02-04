height = [1,3,7,5,3,2,6,9,1]
cantidad_max = 0
l , r = 0 , len(height) - 1
while l < r :
    
    cantidad = min(height[l] , height[r]) * (r - l)
    cantidad_max = max(cantidad_max,cantidad)
    
    if height[l] < height[r]:
        l += 1
    else:
        r -= 1
        
print(cantidad_max)