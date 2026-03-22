# Group Anagrams
# Given a list of strings, group the anagrams together.
# Anagrams are words that share the same letters (e.g., "eat" and "tea").

palabras = ["eat","tea","tan","ate","nat","bat"]

res = {}  # key: sorted letters as tuple, value: list of anagrams

for palabra in palabras:
    # Sort the letters to create a common key for all anagrams
    letras = tuple(sorted(palabra))

    if letras in res:
        res[letras].append(palabra)
    else:
        res[letras] = [palabra]

print(list(res.values()))
