nums = [3, 0, 1, 0, 2]
ceros = 0
respuesta = []
for num in nums:
    if num == 0:
        ceros += 1
    else:
        respuesta.append(num)

print(respuesta + [0] * ceros)