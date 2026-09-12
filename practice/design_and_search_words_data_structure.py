class TrieNode:
    def __init__(self):
        # Cada nodo guarda sus siguientes letras y si aquí termina una palabra.
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        # Paso 1: el trie comienza con una raíz vacía.
        self.root = TrieNode()

    def addWord(self, word):
        # Paso 2: recorre la palabra desde la raíz.
        temporal = self.root
        for letra in word:
            # Crea el camino solo cuando la letra todavía no existe.
            if letra not in temporal.children:
                temporal.children[letra] = TrieNode()

            temporal = temporal.children[letra]

        # Marca el último nodo para distinguir palabras completas de prefijos.
        temporal.is_word = True

    def search(self, word):
        def dfs(indice, nodo: TrieNode):
            # Paso 3: al consumir el patrón, confirma que sea una palabra completa.
            if indice == len(word):
                return nodo.is_word
            
            # Paso 4: el comodín prueba recursivamente cada letra disponible.
            if word[indice] == ".":
                for letra in nodo.children.values():
                    resultado = dfs(indice + 1, letra)

                    if resultado:
                        return True
                return False
            
            # Paso 5: una letra normal solo continúa por su rama correspondiente.
            if word[indice] in nodo.children:
                return dfs(indice+1, nodo.children[word[indice]])
            return False

        # Inicia la búsqueda desde la primera letra y la raíz del trie.
        return dfs(0,self.root)
