class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unico = 0

        for numero in nums:
            unico ^= numero

        return unico


if __name__ == "__main__":
    solucion = Solution()

    assert solucion.singleNumber([2, 2, 1]) == 1
    assert solucion.singleNumber([4, 1, 2, 1, 2]) == 4
    assert solucion.singleNumber([1]) == 1

    print("Todas las pruebas pasaron.")
