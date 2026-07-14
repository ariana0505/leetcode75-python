grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

contador =   0
filas  = len(grid1)
columnas  =  len(grid1[0])

def hundir(r,c):
    if r<0 or r>=filas or c<0  or c>= columnas:
        return
    if  grid1[r][c]  != "1":
        return
    grid1[r][c]  = "0"

    hundir(r+1,c)
    hundir(r-1,c)
    hundir(r,c-1)
    hundir(r,c+1)

for  r in range(filas):
    for  c in  range(columnas):
        if grid1[r][c] ==  "1":
            contador +=1
            hundir(r,c)
