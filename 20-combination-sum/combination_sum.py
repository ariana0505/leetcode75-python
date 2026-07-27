

def dfs(i: int, candidates: list[int], target: int, cur: list[int], total: int, res: list[list[int]]) -> None:
    if total == target:
        res.append(cur.copy())
        return
    if i >= len(candidates) or total > target:
        return

    # Include the current candidate (it can be reused)
    cur.append(candidates[i])
    dfs(i, candidates, target, cur, total + candidates[i], res)

    # Skip the current candidate and move to the next
    cur.pop()
    dfs(i + 1, candidates, target, cur, total, res)


candidates: list[int] = [2, 3]
target: int = 7
res: list[list[int]] = []

dfs(0, candidates, target, [], 0, res)
print(res)
