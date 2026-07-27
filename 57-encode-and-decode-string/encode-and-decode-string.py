

def encode(strs: list[str]) -> str:
    res: str = ""
    for word in strs:
        res += str(len(word)) + "#" + word
    return res


def decode(strg: str) -> list[str]:
    res: list[str] = []
    i: int = 0

    while i < len(strg):
        j = i

        # Find the '#' delimiter
        while strg[j] != "#":
            j += 1

        # Get the length of the next word
        length: int = int(strg[i:j])

        # Extract the word
        res.append(strg[j + 1 : j + 1 + length])

        # Advance the pointer past the current word
        i = j + 1 + length

    return res
