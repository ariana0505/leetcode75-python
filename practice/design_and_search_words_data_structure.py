class TrieNode:
    def __init__(self):
        self.hijos = {} # => letra : nodo
        self.es_palabra = False
class WordDictionary :
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, palabra):
        cur = self.root
        for letra in palabra:
            if letra not in cur.hijos.keys():
                cur.hijos[letra] = TrieNode()
                cur = cur.hijos[letra]
            else:
                cur = cur.hijos[letra]
        cur.es_palabra = True

    def search(self,palabra):
        cur = self.root
        def dfs(nodo:TrieNode, i):
            if len(palabra) == i:
                return nodo.es_palabra
            if palabra[i] in nodo.hijos.keys():
                return dfs(nodo.hijos[palabra[i]], i+1)
            if palabra[i] == ".":
                for nodo in nodo.hijos.values():
                    if dfs(nodo, i+1):
                        return True
            return False
        return dfs(cur,0)
        