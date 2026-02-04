# rob1: máximo dinero robado hasta la casa i-2
# rob2: máximo dinero robado hasta la casa i-1
rob1, rob2 = 0, 0
nums = [2,7,9,3,1]

for n in nums:
    # Opción 1: robar esta casa → n + rob1
    # Opción 2: no robar esta casa → rob2
    temp = max(n + rob1, rob2)

    # Desplazamos los estados para la siguiente iteración
    rob1 = rob2      # lo que era i-1 ahora será i-2
    rob2 = temp      # el mejor resultado actual

# rob2 contiene el máximo dinero que se puede robar
resultado = rob2
print(resultado)