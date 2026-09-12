intervalos = [[1,2], [2,3], [3,4], [1,3]]

# Paso 1: ordenamos por el final para conservar primero el intervalo que antes termina.
intervalos.sort(key=lambda x: x[1])

# Paso 2: comenzamos sin eliminaciones y usamos el primer final como referencia.
eliminados = 0
fin_anterior = intervalos[0][1]

# Paso 3: comparamos cada intervalo con el último que decidimos conservar.
for inicio, fin in intervalos[1:]:
    if inicio < fin_anterior:
        # Hay superposición, así que eliminamos el intervalo actual.
        eliminados += 1
    else:
        # No se superponen; conservamos el actual y actualizamos la referencia.
        fin_anterior = fin

# Paso 4: mostramos la cantidad mínima de intervalos eliminados.
print(eliminados)
