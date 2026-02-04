days = [5, 7, 2, 1, 7]
ganancia = 0
compra, venta = 0, 1

while venta < len(days):
    if days[venta] > days[compra]:  
        nueva_ganancia = days[venta] - days[compra]
        ganancia = max(ganancia, nueva_ganancia)
    else:
        compra = venta  

    venta += 1

print(ganancia)
