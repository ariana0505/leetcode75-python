board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

filas  = len(board)
columnas  = len(board[0])

def dfs(r,c,k):
    if  k  ==  len(word):
        return True
    if  r < 0 or r >= filas or c  <  0 or c  >= columnas:
        return  False
    if word[k] != board[r][c]:
        return False
    if board[r][c]  ==  "#":
        return  False
    temp =  board[r][c]
    board[r][c] =  "#"
    encontrado =  (dfs(r+1,c,k+1) or dfs(r - 1,c,k+1) or dfs(r,c+1,k+1) or dfs(r,c-1,k+1))
    board[r][c] = temp
    return encontrado

visto  =   False

for r  in  range(filas):
    for c  in range(columnas):
        if  dfs(r,c,0):
            visto = True
            break
    if visto:
        break

print(visto)