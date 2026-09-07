intervalos = [[1,2], [2,3], [3,4], [1,3]]
intervalos.sort(key=lambda x: x[1])
eliminados = 0 
fin_anterior = intervalos[0][1]
for inicio , fin in intervalos[1:]:
    if inicio < fin_anterior:
        eliminados += 1
    else:
        fin_anterior = fin
print(eliminados)