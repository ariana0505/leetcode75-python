nums = [3,2,4]
target = 6
memoria = {}

respuesta = []
for i,num in enumerate(nums):
    necesito = target - num
    if necesito in memoria:
        respuesta.append(memoria[necesito])
        respuesta.append(i)
        break
    else:
        memoria[num] = i
print(respuesta)
