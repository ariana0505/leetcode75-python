from typing import List


def dfs(i: int, candidates: List[int], target: int, cur: List[int], total: int, res: List[List[int]]) -> None:
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


candidates: List[int] = [2, 3]
target: int = 7
res: List[List[int]] = []

dfs(0, candidates, target, [], 0, res)
print(res)
