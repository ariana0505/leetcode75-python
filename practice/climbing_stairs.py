n = 2
num1 = 1
num2 = 1
for i  in range(n):
    temp = max(num1 + i ,num2)
    num1 = num2
    num2 = temp
print(num2)