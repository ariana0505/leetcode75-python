
# rob1: max money robbed up to house i-2
# rob2: max money robbed up to house i-1
rob1: int = 0
rob2: int = 0
houses: list[int] = [2, 7, 9, 3, 1]

for money in houses:
    # Option 1: rob this house -> money + rob1
    # Option 2: skip this house -> rob2
    temp: int = max(money + rob1, rob2)

    # Shift states for the next iteration
    rob1 = rob2      # previous i-1 becomes i-2
    rob2 = temp      # current best result

# rob2 holds the maximum money that can be robbed
result: int = rob2
print(result)
