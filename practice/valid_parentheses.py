from collections import deque
s = "()[]{}"

pila =  deque()
diccinario  = {")":"(",
               "}":"{",
               "]":"["
               }

for  simbol in s:
    if simbol  in diccinario.keys():
        if pila and diccinario[simbol]  == pila.pop():
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