class TrieNode:
    def  __init__(self):
        self.children = {}
        self.endOfword  = False

class Trie:

    def __init__(self):
        self.root =  TrieNode()
    
    def insert(self, word:str ):
        cur = self.root
        for letra  in  word:
            if  letra not in cur.children:
                cur.children[letra]  = TrieNode()
            cur = cur.children[letra]
        cur.endOfword  = True
    
    def search(self, word):
        cur  = self.root
        for letra  in word:
            if  letra not in cur.children:
                return False
            cur = cur.children[letra]
        return  cur.endOfword
    
    def startswith(self, prefix):
        cur  = self.root
        for letra in prefix:
            if letra  not   in cur.children:
                return   False
            cur  = cur.children[letra]
        return  True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # False
    print(trie.startswith("app"))  # True
    print(trie.startswith("xyz"))  # False