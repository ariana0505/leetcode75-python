nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
n = len(nums)
suma_esperada = n * (n + 1) // 2
suma_verdadera = sum(nums)

print(suma_esperada -  suma_verdadera)