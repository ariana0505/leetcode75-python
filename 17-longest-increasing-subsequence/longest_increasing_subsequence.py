import bisect

nums = [0, 1, 0, 3, 2, 3]

tails = []

for num in nums:
    lugar_indicado = bisect.bisect_left(tails, num)

    if lugar_indicado == len(tails):
        tails.append(num)
    else:
        tails[lugar_indicado] = num

print(len(tails))