def longest_common_subsequence(text1: str, text2: str) -> int:
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    previous = [0] * (len(text2) + 1)
    for char1 in text1:
        current = [0]
        for index, char2 in enumerate(text2, start=1):
            if char1 == char2:
                current.append(previous[index - 1] + 1)
            else:
                current.append(max(previous[index], current[-1]))
        previous = current
    return previous[-1]


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    print(3)
