class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        temporal = self.root
        for letra in word:
            if letra not in temporal.children:
                temporal.children[letra] = TrieNode()

            temporal = temporal.children[letra]
        temporal.is_word = True
    def search(self, word):
        def dfs(indice, nodo: TrieNode):
            if indice == len(word):
                return nodo.is_word
            
            if word[indice] == ".":
                for letra in nodo.children.values():
                    resultado = dfs(indice + 1, letra)

                    if resultado:
                        return True
                return False
            
            if word[indice] in nodo.children:
                return dfs(indice+1, nodo.children[word[indice]])
            return False
        return dfs(0,self.root)
    