nums = [-2,1,-3,4,-1,2,1,-5,4]
sumaMaxima = nums[0]
sumaActual = 0

for i in range(len(nums)):
    sumaActual += nums[i]

    # Si la suma actual es negativa, reiniciamos a 0
    if sumaActual < 0:
        sumaActual = 0

    print(sumaActual)
    sumaMaxima = max(sumaMaxima, sumaActual)
    print(sumaMaxima)

print(sumaMaxima)
