# Jump Game: determinar si se puede llegar al ultimo indice
nums = [2, 3, 1, 1, 4]

# meta es el indice que necesitamos alcanzar, empezamos desde el final
meta = len(nums) - 1

# recorremos de derecha a izquierda
for i in range(len(nums) - 2, -1, -1):
    # si desde la posicion i podemos alcanzar la meta, movemos la meta
    if i + nums[i] >= meta:
        meta = i

print(meta == 0)
