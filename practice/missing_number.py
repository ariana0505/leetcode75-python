nums = [9,6,4,2,3,5,7,0,1]
n = len(nums)
print(n)
suma_nums = sum(nums)
suma_esperada =(n * (n + 1))/2
print(int(suma_esperada - suma_nums))