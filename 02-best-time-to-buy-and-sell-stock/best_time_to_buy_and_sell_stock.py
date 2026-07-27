
days: list[int] = [5, 7, 2, 1, 7]
profit: int = 0
buy: int
sell: int
buy, sell = 0, 1

while sell < len(days):
    if days[sell] > days[buy]:
        new_profit: int = days[sell] - days[buy]
        profit = max(profit, new_profit)
    else:
        buy = sell  # Found a lower price, update buy day

    sell += 1

print(profit)
