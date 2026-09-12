class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """Agrega una palabra al Trie."""
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.is_word = True

    def search(self, word: str) -> bool:
        """Indica si existe una palabra que coincide con el patron dado."""
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.is_word

            letter = word[index]

            if letter != ".":
                next_node = node.children.get(letter)
                return next_node is not None and dfs(index + 1, next_node)

            return any(dfs(index + 1, child) for child in node.children.values())

        return dfs(0, self.root)


if __name__ == "__main__":
    word_dictionary = WordDictionary()
    for word in ("bad", "dad", "mad"):
        word_dictionary.addWord(word)

    assert word_dictionary.search("pad") is False
    assert word_dictionary.search("bad") is True
    assert word_dictionary.search(".ad") is True
    assert word_dictionary.search("b..") is True
    assert word_dictionary.search("...") is True
    assert word_dictionary.search("..") is False

    print("Todas las pruebas pasaron.")
