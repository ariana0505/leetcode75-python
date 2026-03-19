nums = [-2,1,-3,4,-1,2,1,-5,4]
sumaMaxima = nums[0]
sumaActual = nums[0]

for i in range(1, len(nums)):
    sumaActual = max(nums[i], sumaActual + nums[i])
    sumaMaxima = max(sumaMaxima, sumaActual)

print(sumaMaxima)
# <arreglado>
# Se reseteaba sumaActual a 0 cuando era negativa, lo que causaba que con arrays
# totalmente negativos (ej: [-3,-2,-5,-1]) devolviera 0 en vez del mayor negativo (-1).
# Se corrigio usando Kadane's: sumaActual = max(nums[i], sumaActual + nums[i])
#
# The old code reset sumaActual to 0 when negative, so for all-negative arrays
# (e.g. [-3,-2,-5,-1]) it returned 0 instead of the largest negative (-1).
# Fixed using Kadane's algorithm: sumaActual = max(nums[i], sumaActual + nums[i])
