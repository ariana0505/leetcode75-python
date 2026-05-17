class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str):
        cur = self.root
        for letra in word:
            if letra not in cur.children:
                cur.children[letra]  =  TrieNode()
            cur =  cur.children[letra]
        cur.endOfword = True
    
    def search(self,word:str):
        cur =  self.root
        for letra  in  word:
            if letra not in cur.children:
                return False
            cur = cur.children[letra]
        return cur.endOfword
    
    def startsWith(self,word:str):
        cur =  self.root
        for letra  in  word:
            if letra not in cur.children:
                return False
            cur = cur.children[letra]
        return True


if __name__ == "__main__":
    # Ejemplo del enunciado
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True       # True
    assert trie.search("app") is False        # False
    assert trie.startsWith("app") is True     # True
    trie.insert("app")
    assert trie.search("app") is True         # True

    # Casos extra
    assert trie.startsWith("ap") is True
    assert trie.startsWith("b") is False
    assert trie.search("appl") is False

    print("Todos los tests pasaron")