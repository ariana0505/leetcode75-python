palabras = ["eat","tea","tan","ate","nat","bat"]

diccionario = {}


for palabra in  palabras:
    letras =  tuple(sorted(palabra))
    if  letras in diccionario:
        diccionario[letras].append(palabra)
    else:
        diccionario[letras] = [palabra]
print(list(diccionario.values()))