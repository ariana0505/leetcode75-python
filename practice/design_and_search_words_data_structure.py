class TrieNode:
    def __init__(self):
        self.hijos = {} # -> "letra" : nodo
        self.es_palabra = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, palabra):
        nodo = self.root
        for letra in palabra:
            if letra not in nodo.hijos:
                nodo.hijos[letra] = TrieNode()
                nodo = nodo.hijos[letra]
            else:
                nodo = nodo.hijos[letra]
        
        nodo.es_palabra = True

    def search(self,palabra):
        cur = self.root
        def dfs(nodo:TrieNode,i):
            if i  == len(palabra) :
                return nodo.es_palabra
            if palabra[i] in nodo.hijos:
                nodo = nodo.hijos[palabra[i]]
                return dfs(nodo,i+1)
            if palabra[i] == ".":
                for nodo in nodo.hijos.values():
                    resultado = dfs(nodo, i + 1)
                    if resultado == True:
                        return True
            return False
        return dfs(cur, 0)