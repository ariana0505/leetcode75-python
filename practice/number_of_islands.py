

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        pass


if __name__ == "__main__":
    # Ejemplo 1 -> 1 isla (todo esta conectado)
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    # Ejemplo 2 -> 3 islas ((2,2) y (3,3) solo se tocan en diagonal)
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    # Puras diagonales -> 5 islas
    grid3 = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"],
    ]

    # Todo agua -> 0 islas
    grid4 = [
        ["0", "0"],
        ["0", "0"],
    ]

    # Una sola celda de tierra -> 1 isla
    grid5 = [["1"]]

    casos = [(grid1, 1), (grid2, 3), (grid3, 5), (grid4, 0), (grid5, 1)]

    for i, (grid, esperado) in enumerate(casos, start=1):
        obtenido = Solution().numIslands(grid)
        estado = "OK" if obtenido == esperado else "FALLA"
        print(f"caso {i}: esperado={esperado}  obtenido={obtenido}  -> {estado}")
