class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    if not board or not board[0] or not words:
        return []

    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.word = word

    rows, cols = len(board), len(board[0])
    result = []

    def search(row: int, col: int, node: TrieNode) -> None:
        char = board[row][col]
        next_node = node.children.get(char)
        if next_node is None:
            return

        if next_node.word is not None:
            result.append(next_node.word)
            next_node.word = None

        board[row][col] = "#"
        for row_delta, col_delta in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_delta
            next_col = col + col_delta
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if board[next_row][next_col] != "#":
                    search(next_row, next_col, next_node)
        board[row][col] = char

        if not next_node.children and next_node.word is None:
            del node.children[char]

    for row in range(rows):
        for col in range(cols):
            search(row, col, root)
    return result


if __name__ == "__main__":
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]
    assert set(find_words(board, words)) == {"oath", "eat"}
    print(find_words(board, words))
