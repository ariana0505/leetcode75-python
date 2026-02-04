from typing import List

def dfs(i, candidates, target, cur, total, res):
    if total == target:
        res.append(cur.copy())
        return
    if i >= len(candidates) or total > target:
        return

    # tomar el candidato actual (se puede repetir)
    cur.append(candidates[i])
    dfs(i, candidates, target, cur, total + candidates[i], res)

    # no tomarlo, pasar al siguiente
    cur.pop()
    dfs(i + 1, candidates, target, cur, total, res)

candidates = [2,3]
target = 7
res = []

dfs(0, candidates, target, [], 0, res)
print(res)