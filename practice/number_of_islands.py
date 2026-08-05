class Solution:
    def numIslands(self, grid):
        filas = len(grid)
        columnas = len(grid[0])
        islas = 0

        def hundir_isla(fila, columna):
            if fila < 0 or columna < 0 or fila >= filas or columna >= columnas or grid[fila][columna] != "1":
                return
            grid[fila][columna] = "0"
            hundir_isla(fila - 1, columna)
            hundir_isla(fila + 1, columna)
            hundir_isla(fila, columna - 1)
            hundir_isla(fila, columna + 1)

        for fila in range(filas):
            for columna in range(columnas):
                if grid[fila][columna] == "1":
                    islas += 1
                    hundir_isla(fila, columna)

        return islas


if __name__ == "__main__":
    solution = Solution()

    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(solution.numIslands(grid1))  # 1

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(solution.numIslands(grid2))  # 3

    grid3 = [
        ["0","0","0"],
        ["0","0","0"],
        ["0","0","0"]
    ]
    print(solution.numIslands(grid3))  # 0

    grid4 = [
        ["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]
    ]
    print(solution.numIslands(grid4))  # 1

    grid5 = [["1"]]
    print(solution.numIslands(grid5))  # 1

    grid6 = [["0"]]
    print(solution.numIslands(grid6))  # 0

    grid7 = [
        ["1","0","1","0","1"]
    ]
    print(solution.numIslands(grid7))  # 3
