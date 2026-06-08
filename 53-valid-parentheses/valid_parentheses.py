from  collections import deque
s = "([])"

pila = deque()

validacion = {")" : "(","]":"[","}" :"{"}

for caracter  in  s:
    if caracter in validacion.keys():
        if pila  and  validacion[caracter]  == pila[-1]:
            pila.pop()
        else:
            print(False)
            break
    
    if caracter  not  in validacion:
        pila.append(caracter)
else:
    if not pila:
        print(True)
    else:
        print(False)