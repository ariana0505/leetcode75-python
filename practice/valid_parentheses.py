from  collections   import deque
s = "([])"

pila  =  deque()

diccionario = {"]":"[",
               "}":"{",
               ")":"("}

for simbol in s:
    if simbol in diccionario.keys():
        if pila and diccionario[simbol]  == pila.pop() :
            pass
        else:
            print(False)
            break 
    else:
        pila.append(simbol)
    
else:
    if not pila:
        print(True)
    else:
        print(False)