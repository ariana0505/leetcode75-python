n = 8 
uno = 1
dos = 1

# Repetimos el proceso n veces
for i in range(n):
    # Guardamos el valor actual de 'uno'
    temp = uno

    # Sumamos los dos números
    uno = uno + dos

    # Actualizamos 'dos' con el valor anterior
    dos = temp

# Mostramos el último valor guardado
print(temp)