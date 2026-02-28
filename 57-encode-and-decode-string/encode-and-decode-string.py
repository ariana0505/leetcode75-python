def encode(strs):
    res = ""
    for palabra in strs:
        res += str(len(palabra)) + "#" + palabra
    return res


def decode(strg):
    res = []
    i = 0

    while i < len(strg):
        j = i

        # Buscar el #
        while strg[j] != "#":
            j += 1

        # Obtener longitud
        largo = int(strg[i:j])

        # Extraer palabra
        res.append(strg[j + 1 : j + 1 + largo])

        # Mover puntero
        i = j + 1 + largo

    return res