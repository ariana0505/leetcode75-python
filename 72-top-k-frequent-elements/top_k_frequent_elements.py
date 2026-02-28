k = 2 #dos elementos mas frecuentes
nums=[1,1,1,2,2,3]
freq = [[] for i in range(len(nums) + 1)]
count ={}

for num in nums:
    count[nums] = 1 + count.get(nums, 0)

# aplicamos Bucket Sort    
for n, c in count.items(): #(1,3), (2,2), (3,1) -> numero, frecuencia
    freq[c].append(n) # freq = [[], [3], [2], [1], [], [], []]

res = []
for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)