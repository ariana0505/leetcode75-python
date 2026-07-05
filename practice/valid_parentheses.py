from  collections  import  deque
simbols   =  "()[]{}"
pila =  deque()

dicionario = {"]": "[", "}":"{",")":"("}

for simbol  in simbols:
    if simbol  in dicionario.keys():
        if  pila and dicionario[simbol] == pila.pop():
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