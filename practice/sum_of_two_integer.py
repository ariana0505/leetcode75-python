num1  = 5
num2  = 4
while  num2 != 0 :
    temp =  (num1 & num2)  << 1
    num1 =  num2  ^  num1
    num2 = temp
print(num1)