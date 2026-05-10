cadena  = "aaaba"
resultado  = 0

for i in range(len(cadena)):
    # PARA LOS  IIMPARES
    l = r  = i
    while   l >= 0 and r< len(cadena) and  cadena[l]  == cadena[r]:
        #encontramos resulctado impar:
        resultado += 1
        l -=  1
        r +=  1
    #encontramos tds los impares

    #para los pares
    l  =  i
    r  =  i  +  1
    while   l >= 0 and r< len(cadena) and  cadena[l]  == cadena[r]:
        resultado += 1
        l -=  1
        r +=  1

print(resultado)