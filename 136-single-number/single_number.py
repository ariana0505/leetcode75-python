nums = [4,1,2,1,2]
diccionario = {}
for numero in nums:
    diccionario[numero] = diccionario.get(numero, 0) + 1

for numero, conteo in diccionario.items():
    if conteo == 1:
        print(numero)
        break